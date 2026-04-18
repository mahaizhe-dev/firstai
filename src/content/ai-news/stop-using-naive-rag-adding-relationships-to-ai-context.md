---
title: 'Stop using naive RAG – adding relationships to AI context'
description: 'I’ve been working a lot with RAG systems recently, and kept running into the same issue: they retrieve relevant chunks, but lose the relationships between them.This becomes a problem pretty quickly wh'
pubDate: 2026-04-17T23:35:02
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47811753'
tags: []
---

I’ve been working a lot with RAG systems recently, and kept running into the same issue: they retrieve relevant chunks, but lose the relationships between them.This becomes a problem pretty quickly when dealing with real systems (docs, APIs, infra), where understanding how things connect matters more than just finding similar text.So I built Mindex: https://usemindex.dev/It combines semantic search with a knowledge graph layer, so instead of returning isolated chunks, it can connect documents and surface how they relate.It works via CLI and MCP, so you can plug it directly into tools like Claude Code, Cursor, or your own agents.I also added a visual comparison showing naive RAG vs graph-based retrieval, which makes the difference clearer.Would love feedback — especially from people building with RAG or working on developer tooling. Comments URL: https://news.ycombinator.com/item?id=47811753 Points: 2 # Comments: 0
