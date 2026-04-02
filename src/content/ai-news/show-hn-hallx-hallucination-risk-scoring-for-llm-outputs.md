---
title: 'Show HN: Hallx – Hallucination risk scoring for LLM outputs'
description: 'I got tired of LLM outputs silently failing in pipelines, so I built a small scoring layer around it.It checks three things before your output moves forward: does it match the schema you expected is i'
pubDate: 2026-04-02T15:35:20
source: 'Hacker News'
sourceUrl: 'https://github.com/dhanushk-offl/hallx'
tags: []
---

I got tired of LLM outputs silently failing in pipelines, so I built a small scoring layer around it.It checks three things before your output moves forward: does it match the schema you expected is it consistent across runs does it actually align with the context you providedReturns a confidence score and a risk level. That's mostly it.Works with OpenAI, Anthropic, Gemini, Ollama and a few others. Sync and async both supported. It's heuristic, not a guarantee. If your context is bad, the scores will be too. Hit a star, if you found this useful.Try now: pip install hallx Comments URL: https://news.ycombinator.com/item?id=47615874 Points: 1 # Comments: 0
