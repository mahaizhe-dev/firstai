---
title: 'Show HN: A memory layer for AI agents that organizes itself'
description: 'I kept running into the same issue building agents:Memory just grows forever. Nothing gets cleaned up.So I tried something different - treating memory like a system that maintains itself.StixDB is a s'
pubDate: 2026-04-03T19:31:28
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47631079'
tags: []
---

I kept running into the same issue building agents:Memory just grows forever. Nothing gets cleaned up.So I tried something different - treating memory like a system that maintains itself.StixDB is a small experiment around that idea.Instead of just storing facts, it runs a background loop that:- merges similar entries - tracks which ones are actually used - gradually reduces the importance of unused onesOver time, the memory graph reshapes itself.One interesting constraint:* The background process only touches a small batch each cycle (64 nodes), so the cost stays predictable even as memory grows.It works fully local (no API key), and you can still layer an LLM on top if needed.I’m not sure if this is genuinely useful or just an over-engineered idea.Would love to hear how others are handling long-term memory in agents.Github: https://github.com/Pr0fe5s0r/StixDB Comments URL: https://news.ycombinator.com/item?id=47631079 Points: 2 # Comments: 0
