---
title: 'Show HN: Vibe-budget – CLI to estimate LLM costs before you start vibe coding'
description: 'I built vibe-budget because I kept burning tokens without knowing the cost upfront. You describe your project in plain English (or Spanish), and it detects the tasks involved, estimates token usage, a'
pubDate: 2026-03-14T03:09:05
source: 'Hacker News'
sourceUrl: 'https://www.npmjs.com/package/vibe-budget'
tags: []
---

I built vibe-budget because I kept burning tokens without knowing the cost upfront. You describe your project in plain English (or Spanish), and it detects the tasks involved, estimates token usage, and compares real-time prices across 85+ models via OpenRouter.Example: vibe-budget plan ecommerce with stripe oauth and supabaseIt detects 4 tasks, estimates ~497k tokens, and shows you the cheapest, best quality-price, and premium model options side by side.It also has a scan command — point it at an existing codebase and it estimates how many tokens it would cost to refactor or extend it with AI.No API key required. Prices are fetched live from OpenRouter with a 1-hour cache fallback.npm install -g vibe-budgetDocs: https://gaboexe0.github.io/vibe-budget/ Repo: https://github.com/gaboexe0/vibe-budget Comments URL: https://news.ycombinator.com/item?id=47372921 Points: 1 # Comments: 0
