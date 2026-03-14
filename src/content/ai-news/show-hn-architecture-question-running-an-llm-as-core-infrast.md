---
title: 'Show HN: Architecture question: running an LLM as core infrastructure'
description: 'I''ve been experimenting with running an LLM not as a chatbot but as the core runtime of a business system, and I''m curious how others approach this.The idea is that the model doesn''t just answer quest'
pubDate: 2026-03-14T18:14:10
source: 'Hacker News'
sourceUrl: 'https://automazionezeli.com'
tags: []
---

I've been experimenting with running an LLM not as a chatbot but as the core runtime of a business system, and I'm curious how others approach this.The idea is that the model doesn't just answer questions but orchestrates tools and interacts with real application logic.The architecture I'm currently testing includes:Runtimetool orchestration parallel tool execution loop detection circuit breaker / timeout guards token budgeting Contextcontext compression dynamic token ceiling Cachingdeterministic LLM response cache semantic cache using pgvector Memoryshort-term session memory longer-term semantic memory Evaluationprompt evaluation set to test tool reasoning and failures I'm trying to figure out which parts are actually necessary in production and which ones are over-engineering.For people building LLM systems beyond simple chat interfaces:how do you handle tool orchestration? do you implement memory layers or just rely on context? are semantic caches worth it in practice? Curious to hear how others structure this. Comments URL: https://news.ycombinator.com/item?id=47379441 Points: 1 # Comments: 0
