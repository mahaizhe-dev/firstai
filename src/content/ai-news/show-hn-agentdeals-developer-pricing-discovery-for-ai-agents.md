---
title: 'Show HN: AgentDeals – Developer pricing discovery for AI agents'
description: 'When Claude Code or Cursor recommends you sign up for Railway, it has no idea that Render has a better free tier, or if Railway just killed its free plan last week. Your agent is making infrastructure'
pubDate: 2026-03-19T13:42:04
source: 'Hacker News'
sourceUrl: 'https://github.com/robhunter/agentdeals'
tags: []
---

When Claude Code or Cursor recommends you sign up for Railway, it has no idea that Render has a better free tier, or if Railway just killed its free plan last week. Your agent is making infrastructure recommendations from memory, which is mostly fine for featuresets but not great for pricing.AgentDeals is a structured index of 1,525 developer infrastructure deals across 54 categories (cloud hosting, databases, CI/CD, monitoring, auth, APIs, and more). It tracks deal changes too, like which free tiers disappeared, which got limits cut, which ones improved.Three ways to use it: 1. Browse: https://agentdeals.dev 2. REST API: /api/offers, /api/categories, /api/changes (no auth) 3. MCP server: connect from Claude, Cursor, VS Code Copilot, or any MCP clientThe MCP server has four intent-based tools - search_deals, plan_stack, compare_vendors, track_changes - so your agent can query deals as part of its normal workflow. "Find me free database hosting" or "what changed in the last 30 days?" with structured responses.Each entry has a verified_date showing when we last checked the pricing page, so if the index goes stale at least you know about it. Open source (see link), plus a site with some more info: https://agentdeals.devHopefully this saves you a buck or two. Comments URL: https://news.ycombinator.com/item?id=47439295 Points: 1 # Comments: 0
