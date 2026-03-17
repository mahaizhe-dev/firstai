---
title: 'Show HN: Need is a CLI tool discovery as an MCP server'
description: 'need is an MCP server that gives AI agents access to a searchable index of 10,000+ CLI tools. The agent searches in plain English, installs the best match (restricted to brew/npm/pip/cargo/apt so no a'
pubDate: 2026-03-17T15:05:10
source: 'Hacker News'
sourceUrl: 'https://www.agentneeds.dev/'
tags: []
---

need is an MCP server that gives AI agents access to a searchable index of 10,000+ CLI tools. The agent searches in plain English, installs the best match (restricted to brew/npm/pip/cargo/apt so no arbitrary shell), and reports whether it worked. Those reports improve rankings for every future search.One command sets it up: npx @agentneeds/need setup - works with Claude Code and Cursor.Search is embeddings + pgvector with a keyword boost and full-text fallback. With no community signals yet, ranking is pure semantic similarity. As people use it, the signal-weighted ranking kicks in.Also works as a plain CLI if you just want to find tools yourself: need "compress video without losing quality"Try some queries and tell me what's ranked wrong that's genuinely the most useful feedback right now. Comments URL: https://news.ycombinator.com/item?id=47413712 Points: 3 # Comments: 0
