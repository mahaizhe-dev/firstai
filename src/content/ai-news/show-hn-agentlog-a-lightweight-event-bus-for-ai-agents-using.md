---
title: 'Show HN: AgentLog – a lightweight event bus for AI agents using JSONL logs'
description: 'I’ve been experimenting with infrastructure for multi-agent systems.I built a small project called AgentLog.The core idea is very simple, topics are just append-only JSONL files.Agents publish events '
pubDate: 2026-03-13T18:39:16
source: 'Hacker News'
sourceUrl: 'https://github.com/sumant1122/agentlog'
tags: []
---

I’ve been experimenting with infrastructure for multi-agent systems.I built a small project called AgentLog.The core idea is very simple, topics are just append-only JSONL files.Agents publish events over HTTP and subscribe to streams using SSE.The system is intentionally single-node and minimal for now.Future ideas I’m exploring: - replayable agent workflows - tracing reasoning across agents - visualizing event timelines - distributed/federated agent logsCurious if others building agent systems have run into similar needs. Comments URL: https://news.ycombinator.com/item?id=47367987 Points: 4 # Comments: 1
