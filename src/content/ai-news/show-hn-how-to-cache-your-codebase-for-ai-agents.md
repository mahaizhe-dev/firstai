---
title: 'Show HN: How to cache your codebase for AI agents'
description: 'The problem is every time an AI agent needs to find relevant files, it either guesses by filename, runs a grep across the whole repo, or reads everything in sight. On any codebase of real size, this w'
pubDate: 2026-03-18T19:17:16
source: 'Hacker News'
sourceUrl: 'https://github.com/kaanozhan/Frame'
tags: []
---

The problem is every time an AI agent needs to find relevant files, it either guesses by filename, runs a grep across the whole repo, or reads everything in sight. On any codebase of real size, this wastes context window, slows down responses, and still misses the connections between related files.With this approach a script runs once at commit time, reads each source file, and builds a semantic map; feature names pointing to files, exports, and API channels. That map gets committed alongside your code as a single JSON file. When an AI agent needs to find something, it queries one keyword and gets back the exact files and interfaces in under a millisecond.What you gain: AI agents that navigate your codebase like they wrote it. No context wasted on irrelevant files. No missed connections between a service and its controller. And since the map regenerates automatically on every commit, it never falls out of sync. I added this to my open sourced agentic development platform, feel free to examine it or use it. Any ideas or contributions are always welcome. Comments URL: https://news.ycombinator.com/item?id=47430211 Points: 1 # Comments: 0
