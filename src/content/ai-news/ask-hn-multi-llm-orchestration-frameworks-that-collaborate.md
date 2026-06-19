---
title: 'Ask HN: Multi-LLM orchestration frameworks that collaborate?'
description: 'Here is my general take: I feel Gemini is excellent at high-level refactoring but riddled with bugs when writing actual code. On the other hand, GPT/Claude excel at coding, but when it comes to refact'
pubDate: 2026-06-19T01:52:36
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48593979'
tags: []
---

Here is my general take: I feel Gemini is excellent at high-level refactoring but riddled with bugs when writing actual code. On the other hand, GPT/Claude excel at coding, but when it comes to refactoring, they tend to stick to minor patches. They love throwing in unnecessary defensive programming just to maintain backward compatibility, or ending up with verbose spaghetti code.My idea is to complement their strengths: let Gemini provide the directional/architectural ideas, and then have GPT/Claude discuss and implement them (in fact, I do this manually all the time, and the results are pretty good).So my question is: Are there any Agent frameworks that can automate this kind of collaboration effectively?I'm well aware of the existing "subagent" features, but in my experience, the AI doesn't always choose to invoke them. Moreover, while the subagent is working, the main model usually just sits there idling. It feels less like actual collaboration and more like a mechanism to prevent outsourced tasks from polluting the main context—at least, that's how it feels to me. Comments URL: https://news.ycombinator.com/item?id=48593979 Points: 1 # Comments: 0
