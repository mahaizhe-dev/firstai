---
title: 'Show HN: I stopped using an LLM gateway and put rate-limits/fallback in-process'
description: 'Sup HN. I built VernLLM cuz every LLM gateaway I looked at, meant adding a network hop just to get rate limiting, multi provider fallback, circuit breaking and other features.Needing to take a whole s'
pubDate: 2026-09-06T12:17:10
source: 'Hacker News'
sourceUrl: 'https://github.com/LakBud/vernLLM'
tags: []
---

Sup HN. I built VernLLM cuz every LLM gateaway I looked at, meant adding a network hop just to get rate limiting, multi provider fallback, circuit breaking and other features.Needing to take a whole seperate service just to deploy, monitor and trust with my API keys is just annoying since my whole tech stack was just TypeScript and Node.VernLLM does the same job within your LLM calls, but its in process instead. Its supports OpenAI-compatible APIs, Anthropic, Gemini and Bedrock providers.I would also argue that the features VernLLM provides is more developed then any other gateaway out there when it comes to resilience and customization.The tradeoff vs a gateaway is that it has no centralized policy across multiple apps or languages so if you want that then its better to use a gateaway instead.Here is the docs for more info: https://vernllm.dev Comments URL: https://news.ycombinator.com/item?id=49585787 Points: 3 # Comments: 1
