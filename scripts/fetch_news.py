#!/usr/bin/env python3
"""
RSS 新闻抓取 + OpenAI 摘要生成脚本
自动从配置的 RSS 源获取新闻，生成中文摘要，写入 Markdown 文件。
"""

import os
import re
import sys
import hashlib
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import yaml
from dateutil import parser as date_parser
from openai import OpenAI

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CONTENT_DIR = PROJECT_ROOT / "src" / "content"


def load_config() -> dict:
    config_path = SCRIPT_DIR / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    if not text:
        text = hashlib.md5(text.encode()).hexdigest()[:10]
    return text[:60]


def make_unique_slug(base_slug: str, output_dir: Path) -> str:
    slug = base_slug
    counter = 1
    while (output_dir / f"{slug}.md").exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


def parse_pub_date(entry) -> datetime:
    for field in ("published", "updated", "created"):
        raw = getattr(entry, field, None) or entry.get(field)
        if raw:
            try:
                dt = date_parser.parse(raw)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt
            except (ValueError, TypeError):
                continue
    return datetime.now(timezone.utc)


def get_entry_content(entry) -> str:
    if hasattr(entry, "summary") and entry.summary:
        return entry.summary
    if hasattr(entry, "content") and entry.content:
        return entry.content[0].get("value", "")
    if hasattr(entry, "description") and entry.description:
        return entry.description
    return ""


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&\w+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def summarize_with_ai(client: OpenAI, title: str, content: str, config: dict, regions: list[str] | None = None) -> dict:
    """Use AI (DeepSeek/OpenAI/etc.) to generate a Chinese summary, extract tags, and classify region."""
    ai_config = config.get("ai", {})
    model = ai_config.get("model", "deepseek-chat")
    max_len = ai_config.get("max_summary_length", 200)

    content_preview = content[:2000]

    region_instruction = ""
    if regions:
        region_list = "、".join(regions)
        region_instruction = f"\n3. 将此新闻归类到以下分栏之一：{region_list}\n"

    region_format = ""
    if regions:
        region_format = "\n分栏：<分栏名称>"

    prompt = f"""你是一位专业的新闻编辑。请根据以下新闻标题和内容，完成以下任务：

1. 用简洁的中文写一段摘要（{max_len}字以内）
2. 提取 2-4 个相关标签关键词{region_instruction}
新闻标题：{title}
新闻内容：{content_preview}

请严格按照以下格式输出，不要添加其他内容：
摘要：<摘要内容>
标签：<标签1>,<标签2>,<标签3>{region_format}"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        reply = response.choices[0].message.content.strip()

        summary = ""
        tags = []
        region = None
        for line in reply.split("\n"):
            line = line.strip()
            if line.startswith("摘要：") or line.startswith("摘要:"):
                summary = line.split("：", 1)[-1].split(":", 1)[-1].strip()
            elif line.startswith("标签：") or line.startswith("标签:"):
                raw_tags = line.split("：", 1)[-1].split(":", 1)[-1].strip()
                tags = [t.strip().strip("#") for t in raw_tags.split(",") if t.strip()]
            elif line.startswith("分栏：") or line.startswith("分栏:"):
                region = line.split("：", 1)[-1].split(":", 1)[-1].strip()
                if regions and region not in regions:
                    region = regions[-1]

        if not summary:
            summary = reply[:max_len]
        return {"summary": summary, "tags": tags, "region": region}

    except Exception as e:
        logger.warning(f"AI summarization failed for '{title}': {e}")
        fallback_summary = strip_html(content)[:max_len]
        return {"summary": fallback_summary or title, "tags": [], "region": None}


def write_markdown(
    output_dir: Path,
    slug: str,
    title: str,
    description: str,
    pub_date: datetime,
    source: str,
    source_url: str,
    tags: list[str],
    body: str,
    region: str | None = None,
):
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = make_unique_slug(slug, output_dir)
    filepath = output_dir / f"{slug}.md"

    tag_list = ", ".join(f"'{t}'" for t in tags)
    date_str = pub_date.strftime("%Y-%m-%dT%H:%M:%S")

    frontmatter_lines = [
        "---",
        f"title: '{title.replace(chr(39), chr(39)+chr(39))}'",
        f"description: '{description.replace(chr(39), chr(39)+chr(39))}'",
        f"pubDate: {date_str}",
        f"source: '{source}'",
    ]
    if source_url:
        frontmatter_lines.append(f"sourceUrl: '{source_url}'")
    if region:
        frontmatter_lines.append(f"region: '{region}'")
    frontmatter_lines.append(f"tags: [{tag_list}]")
    frontmatter_lines.append("---")

    content = "\n".join(frontmatter_lines) + "\n\n" + body + "\n"
    filepath.write_text(content, encoding="utf-8")
    logger.info(f"  Written: {filepath.name}")


def fetch_feed(source: dict) -> list[dict]:
    """Parse an RSS feed and return entries."""
    logger.info(f"  Fetching: {source['name']} ({source['url']})")
    try:
        feed = feedparser.parse(source["url"])
        if feed.bozo and not feed.entries:
            logger.warning(f"  Feed error for {source['name']}: {feed.bozo_exception}")
            return []
        return feed.entries
    except Exception as e:
        logger.warning(f"  Failed to fetch {source['name']}: {e}")
        return []


def process_news(config: dict, category_key: str, output_subdir: str):
    """Process all sources for a given category."""
    category_config = config.get(category_key, {})
    sources = category_config.get("sources", [])
    max_items = category_config.get("max_items", 20)

    if not sources:
        logger.info(f"No sources configured for {category_key}")
        return

    ai_config = config.get("ai", {})
    api_key = os.environ.get("AI_API_KEY", "") or os.environ.get("OPENAI_API_KEY", "")
    base_url = ai_config.get("base_url", "https://api.deepseek.com")
    client = OpenAI(api_key=api_key, base_url=base_url) if api_key else None
    if not client:
        logger.warning("AI_API_KEY not set; using raw content without AI summarization")

    output_dir = CONTENT_DIR / output_subdir
    all_entries = []

    for source in sources:
        entries = fetch_feed(source)
        for entry in entries:
            title = getattr(entry, "title", "Untitled") or "Untitled"
            title = strip_html(title)
            link = getattr(entry, "link", "") or ""
            pub_date = parse_pub_date(entry)
            raw_content = strip_html(get_entry_content(entry))

            all_entries.append({
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "raw_content": raw_content,
                "source_name": source["name"],
            })

    all_entries.sort(key=lambda x: x["pub_date"], reverse=True)
    all_entries = all_entries[:max_items]

    logger.info(f"Processing {len(all_entries)} entries for {category_key}")

    regions = category_config.get("regions")

    for entry in all_entries:
        if client:
            ai_result = summarize_with_ai(client, entry["title"], entry["raw_content"], config, regions=regions)
            description = ai_result["summary"]
            tags = ai_result["tags"]
            region = ai_result.get("region")
        else:
            description = entry["raw_content"][:200] or entry["title"]
            tags = []
            region = regions[-1] if regions else None

        if regions and not region:
            region = regions[-1]

        body_text = entry["raw_content"] if entry["raw_content"] else description
        slug = slugify(entry["title"]) or hashlib.md5(entry["title"].encode()).hexdigest()[:12]

        write_markdown(
            output_dir=output_dir,
            slug=slug,
            title=entry["title"],
            description=description,
            pub_date=entry["pub_date"],
            source=entry["source_name"],
            source_url=entry["link"],
            tags=tags,
            body=body_text,
            region=region,
        )


def cleanup_old_files(config: dict):
    """Remove news files older than max_age_days (skip protected directories)."""
    cleanup_config = config.get("cleanup", {})
    max_age = cleanup_config.get("max_age_days", 7)
    protected = set(cleanup_config.get("protected_dirs", []))
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age)

    for subdir in CONTENT_DIR.iterdir():
        if not subdir.is_dir() or subdir.name in protected:
            continue
        for md_file in subdir.glob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
                for line in text.split("\n"):
                    if line.strip().startswith("pubDate:"):
                        date_str = line.split(":", 1)[1].strip().strip("'\"")
                        file_date = date_parser.parse(date_str)
                        if file_date.tzinfo is None:
                            file_date = file_date.replace(tzinfo=timezone.utc)
                        if file_date < cutoff:
                            md_file.unlink()
                            logger.info(f"  Cleaned up: {md_file.name}")
                        break
            except Exception as e:
                logger.warning(f"  Error processing {md_file.name}: {e}")


def main():
    logger.info("=== News Fetch Script Started ===")
    config = load_config()

    logger.info("--- Fetching AI News ---")
    process_news(config, "ai_news", "ai-news")

    logger.info("--- Fetching World News ---")
    process_news(config, "world_news", "world-news")

    logger.info("--- Cleaning Up Old Files ---")
    cleanup_old_files(config)

    logger.info("=== Done ===")


if __name__ == "__main__":
    main()
