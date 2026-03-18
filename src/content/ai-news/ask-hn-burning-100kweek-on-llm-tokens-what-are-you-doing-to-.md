---
title: 'Ask HN: Burning $100K/week on LLM tokens – what are you doing to cut costs?'
description: 'I run a fleet of AI coding agents (Claude, GPT, Gemini) for our trading infra. Last week the bill hit $103K — mostly context window bloat from long tool traces and system prompts getting re-sent on ev'
pubDate: 2026-03-18T07:19:45
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47422571'
tags: []
---

I run a fleet of AI coding agents (Claude, GPT, Gemini) for our trading infra. Last week the bill hit $103K — mostly context window bloat from long tool traces and system prompts getting re-sent on every turn.Things I have tried so far: - Prompt caching (Anthropic/OpenAI) — helps ~30% but only for cache hits - Smaller models for routine tasks (Haiku for linting, Sonnet for code gen) - Truncating conversation history aggressivelyStill feels like I am leaving money on the table. Specifically interested in:1. Token-level compression before hitting the API — anyone using LLMLingua or similar in production? Real numbers? 2. Smarter context management — routing only relevant context to each agent call instead of dumping everything 3. Self-hosted models for the long tail of simple tasksRunning this through an OpenClaw gateway that proxies to multiple providers, so I have a single choke point where I could plug in compression or caching middleware.Would love to hear what is actually working at scale. Not theoretical — battle-tested approaches that saved real dollars. Comments URL: https://news.ycombinator.com/item?id=47422571 Points: 16 # Comments: 11
