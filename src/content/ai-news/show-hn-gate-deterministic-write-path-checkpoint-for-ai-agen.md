---
title: 'Show HN: Gate – deterministic write-path checkpoint for AI agents'
description: 'The write-path control plane for AI agents.AI agents can read systems freely. The problem is writes — CRM imports, email sends, database updates, refunds. Once the agent does it, you can''t unsee it.Ga'
pubDate: 2026-03-10T13:21:27
source: 'Hacker News'
sourceUrl: 'https://zehrava.com/'
tags: []
---

The write-path control plane for AI agents.AI agents can read systems freely. The problem is writes — CRM imports, email sends, database updates, refunds. Once the agent does it, you can't unsee it.Gate sits between the agent and production. Agents submit an intent, Gate evaluates a YAML policy, and only then issues a signed execution order. No LLM at evaluation time — same input always produces the same output.The flow: POST /v1/intents → policy evaluated → approved/blocked/pending POST /v1/intents/:id/execute → gex_ token (15 min TTL) Worker uses token → reports outcome Full audit trail: proposed → policy_checked → approved → execution_requested → execution_succeeded Comments URL: https://news.ycombinator.com/item?id=47322913 Points: 1 # Comments: 0
