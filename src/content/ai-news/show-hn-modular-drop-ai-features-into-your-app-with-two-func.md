---
title: 'Show HN: Modular – drop AI features into your app with two function calls'
description: 'I kept hitting the same wall at work every time we needed to ship an AI feature. What looked like a week of work turned into picking a model, setting up a vector DB, managing embeddings, wiring up cha'
pubDate: 2026-04-20T01:15:28
source: 'Hacker News'
sourceUrl: 'https://modular.run'
tags: []
---

I kept hitting the same wall at work every time we needed to ship an AI feature. What looked like a week of work turned into picking a model, setting up a vector DB, managing embeddings, wiring up chat history, handling retries — none of it was the actual feature. So I built Modular. You register a function that returns your app's data, then call ai.run() for one-shot features or ai.chat() for stateful conversation. Everything else — context management, embeddings, session history, model routing, retries — is handled. MCP-native from day one. Works with Claude, GPT-4o, and Gemini. Still early — collecting feedback before building the full SDK. Would love to hear if others have hit this same wall, or if you think I'm solving the wrong problem. Comments URL: https://news.ycombinator.com/item?id=47829288 Points: 2 # Comments: 1
