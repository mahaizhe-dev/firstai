---
title: 'Show HN: LLM Memory Storage that scales, easily integrates, and is smart'
description: 'I built a super easy to integrate memory storage and retrieval system for NodeJS projects because I saw a need for information to be shared and persisted across LLM chat sessions (and many other LLM f'
pubDate: 2026-03-16T19:16:23
source: 'Hacker News'
sourceUrl: 'https://github.com/colinulin/mind-palace'
tags: []
---

I built a super easy to integrate memory storage and retrieval system for NodeJS projects because I saw a need for information to be shared and persisted across LLM chat sessions (and many other LLM feature interactions). I tried to keep the barrier to use as low as possible so I included built-in support for major LLMs (GPT, Gemini, and Claude) as well as major vector store providers (Weaviate and Pinecone). The memory store works by ingesting and automatically extracting “memories” (summarized single bits of information) from LLM interactions and vectorizing those. When you want to provide relevant context back to the LLM (before a new chat session starts or even after every user request) you just pass the conversation context to the recall method and an LLM quickly searches the vector store and returns only the most relevant memories. This way, we don’t run context size issues as the history and number of memories grows but we ensure that the LLM always has access to the most important context. There’s a lot more I could talk about (like the deduping system or the extremely configurable pieces of the system), but I’ll leave it at that and point you to the README if you’d like to learn more! Also check out the dev client if you’d like to test out the memory palace yourself! Comments URL: https://news.ycombinator.com/item?id=47403458 Points: 2 # Comments: 0
