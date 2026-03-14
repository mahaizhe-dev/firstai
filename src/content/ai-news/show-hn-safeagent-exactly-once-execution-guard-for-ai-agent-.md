---
title: 'Show HN: SafeAgent – exactly-once execution guard for AI agent side effects'
description: 'LLM agents retry tool calls constantly.Retries can happen because of: - model loops - HTTP timeouts - queue retries - orchestration restartsIf the tool triggers something irreversible you can end up w'
pubDate: 2026-03-14T03:12:33
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47372944'
tags: []
---

LLM agents retry tool calls constantly.Retries can happen because of: - model loops - HTTP timeouts - queue retries - orchestration restartsIf the tool triggers something irreversible you can end up with duplicate side effects:retry → duplicate payment retry → duplicate email retry → duplicate ticket retry → duplicate tradeSafeAgent is a small Python guard that sits between the agent decision and the side effect.Pattern:agent decision → deterministic request_id generated → execution guard checks durable receipt → side effect executes once → future retries return cached receiptThe project started while experimenting with settlement logic for peer-to-peer tournament payouts where duplicate payouts would be catastrophic.Repo:https://github.com/azender1/SafeAgentThere are a few small demos in the repo:- OpenAI-style tool example - LangChain wrapper - CrewAI example - a tournament settlement demo showing retry-safe payoutsCurious how other people building agent systems are handling this today.Are most teams just rolling their own idempotency layer? Comments URL: https://news.ycombinator.com/item?id=47372944 Points: 1 # Comments: 0
