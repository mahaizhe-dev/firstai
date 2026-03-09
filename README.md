# 个人资讯站 (News Hub)

基于 Astro 构建的静态资讯网站，包含 **AI 前沿** 和 **世界局势** 两个频道。支持 RSS 自动聚合 + AI 摘要生成，部署在 GitHub Pages 上，可在微信内分享浏览。

## 功能特性

- **双频道**：AI 新闻/工具教程 + 世界局势新闻
- **自动更新**：GitHub Actions 每 6 小时自动抓取 RSS 并生成内容
- **AI 摘要**：使用 OpenAI API 自动翻译/总结为中文
- **手动教程**：AI 工具教程支持手动编写，持久保存不会被自动更新覆盖
- **微信友好**：移动端响应式设计 + Open Graph 标签，微信内分享体验良好
- **暗色模式**：自动跟随系统主题

## 快速开始

### 1. 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建静态站点
npm run build
```

### 2. 部署到 GitHub Pages

1. 在 GitHub 上创建仓库（如 `news-hub`）
2. 修改 `astro.config.mjs` 中的 `site` 和 `base`：
   ```js
   site: 'https://你的用户名.github.io',
   base: '/news-hub',
   ```
3. 在仓库 Settings > Secrets and variables > Actions 中添加：
   - `OPENAI_API_KEY`：你的 OpenAI API Key
4. 在仓库 Settings > Pages 中将 Source 设为 **GitHub Actions**
5. 推送代码到 GitHub，Actions 会自动构建部署

### 3. 触发内容更新

- **自动**：每 6 小时自动运行（由 GitHub Actions cron 触发）
- **手动**：进入仓库 Actions 页面 > "Update Content & Deploy" > "Run workflow"

## 添加 AI 工具教程

在 `src/content/ai-tutorials/` 目录下创建 `.md` 文件：

```markdown
---
title: '工具名称使用指南'
description: '一句话简介'
pubDate: 2026-03-09
tool: '工具名称'
difficulty: 'beginner'    # beginner / intermediate / advanced
tags: ['标签1', '标签2']
---

正文内容（支持 Markdown 语法）...
```

提交推送后，GitHub Actions 会自动构建并部署更新。

## 配置 RSS 源

编辑 `scripts/config.yaml` 文件：

- `ai_news.sources`：AI 新闻的 RSS 源列表
- `world_news.sources`：世界新闻的 RSS 源列表
- `openai.model`：使用的 AI 模型（默认 `gpt-4o-mini`，成本较低）
- `cleanup.max_age_days`：自动清理超过 N 天的旧新闻

## 项目结构

```
news-hub/
├── .github/workflows/     # GitHub Actions 自动化
├── scripts/               # Python 新闻抓取脚本
│   ├── fetch_news.py      # 主脚本
│   ├── config.yaml        # RSS 源配置
│   └── requirements.txt   # Python 依赖
├── src/
│   ├── content/
│   │   ├── ai-news/       # 自动生成的 AI 新闻
│   │   ├── ai-tutorials/  # 手动编写的工具教程（不会被自动清理）
│   │   └── world-news/    # 自动生成的世界新闻
│   ├── pages/             # 页面路由
│   ├── components/        # UI 组件
│   ├── layouts/           # 页面布局
│   └── styles/            # 全局样式
├── astro.config.mjs       # Astro 配置
└── package.json
```

## 技术栈

- [Astro](https://astro.build/) - 静态站点生成器
- [feedparser](https://feedparser.readthedocs.io/) - RSS 解析
- [OpenAI API](https://platform.openai.com/) - AI 摘要生成
- GitHub Actions - CI/CD
- GitHub Pages - 静态托管
