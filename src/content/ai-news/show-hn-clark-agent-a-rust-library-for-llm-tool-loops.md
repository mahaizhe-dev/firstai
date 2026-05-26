---
title: 'Show HN: Clark-agent, a Rust library for LLM tool loops'
description: 'Hi HN,I wrote clark-agent, a small Rust library for running LLM tool loops.The loop is:context -> model -> tool call -> tool result -> repeatThe parts I wanted typed were:- transcript messages - tool '
pubDate: 2026-05-26T19:19:42
source: 'Hacker News'
sourceUrl: 'https://github.com/clark-labs-inc/clark-agent'
tags: []
---

Hi HN,I wrote clark-agent, a small Rust library for running LLM tool loops.The loop is:context -> model -> tool call -> tool result -> repeatThe parts I wanted typed were:- transcript messages - tool calls - tool results - stream events - tool schemasThe model/provider boundary is a StreamFn trait. Tools implement AgentTool. There are hooks for things like context transforms, tool gates, observers, and follow-up messages. Comments URL: https://news.ycombinator.com/item?id=48284610 Points: 1 # Comments: 0
