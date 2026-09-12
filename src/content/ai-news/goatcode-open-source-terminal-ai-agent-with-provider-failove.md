---
title: 'GoatCode – open-source terminal AI agent with provider failover'
description: 'GoatCode is a single 85 MB binary that runs in your terminal. It brings 180+ LLM providers (or your existing Claude/ChatGPT/Gemini/Copilot subscriptions via OAuth), and when your quota dies mid-sessio'
pubDate: 2026-09-12T09:02:29
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=49670455'
tags: []
---

GoatCode is a single 85 MB binary that runs in your terminal. It brings 180+ LLM providers (or your existing Claude/ChatGPT/Gemini/Copilot subscriptions via OAuth), and when your quota dies mid-session it automatically retries then walks your fallback chain live — switches provider mid-turn, says so, and finishes the answer. No crash, no lost context.What’s new in v2.1.10: - Prompt caching on Anthropic (up to 90% cheaper long sessions; savings shown in /cost) - Inline unified diffs after every write/edit - /rewind — jump transcript + files back to any turn - Parallel subagents (up to 3 task calls fan out concurrently) - /search + goat search — full-text across every saved session - @file Tab completion, /model sonnet aliases - True context meter (real API tokens vs model window) - GOAT MODE (bypass) that actually works: mid-turn switch, prompt resolves YES - Noir theme: deep slate + black-green surfacesInstall: npm install -g goatcode-cli (or grab a static binary from the releases page)Repo: https://github.com/Arhan-w/GoatCode Landing: https://goatcode.vercel.app Comments URL: https://news.ycombinator.com/item?id=49670455 Points: 2 # Comments: 0
