---
title: 'Show HN: Cerea – yet another self-hosted LLM chat front end'
description: 'Here is Cerea, a self-hostable, open-source (Apache 2.0) chat+agent frontend for LLMs. It works alone with any OpenAI-compatible inference provider, but it''s way better when coupled with the model gat'
pubDate: 2026-11-05T21:11:50
source: 'Hacker News'
sourceUrl: 'https://github.com/paoloviviani/Cerea'
tags: []
---

Here is Cerea, a self-hostable, open-source (Apache 2.0) chat+agent frontend for LLMs. It works alone with any OpenAI-compatible inference provider, but it's way better when coupled with the model gateway I'm also developing, Pystino (https://github.com/paoloviviani/Pystino).I came to this after struggling to find a hosted chat interface that was truly open source, that I really enjoyed to use, and that was simple enough to be shared and used by family. In particular, I was looking for something that could provide the smooth and integrated user experience of commercial products for the tasks needed by family (e.g., document editing, form filling, notes and knowledge management), but backed by open models hosted wherever I decide.Then it became richer, now supporting: remote coding agents (wrapping Opencode), delegation and coordination between agents, integration between chat/projects and code agents (this one to me is a pain point for Claude, which I use at work), projects, RAG, rich artifacts support, schedules, and more.You can try it yourself, either cloning the full repo and head to Cerea/kit, or just the deploy kit with a script (https://github.com/paoloviviani/Cerea#quick-start).It's just a docker compose with a ./configure script that helps to generate a sensible .env for the specific scenario. It works in the browser and as a PWA on mobile.I hope you'll enjoy, feel free to reach out for questions. Comments URL: https://news.ycombinator.com/item?id=50384502 Points: 1 # Comments: 0
