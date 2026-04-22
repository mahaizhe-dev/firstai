---
title: 'Show HN: Sift – save AI tokens in Codex/Claude by summarizing command output'
description: 'I made a small skill/script for agentic coding workflows:https://github.com/panpeter/sift-skillThe idea is simple:when a command like cargo test, pytest, npm test, or ./gradlew test prints a lot of ou'
pubDate: 2026-04-22T12:34:18
source: 'Hacker News'
sourceUrl: 'https://github.com/panpeter/sift-skill'
tags: []
---

I made a small skill/script for agentic coding workflows:https://github.com/panpeter/sift-skillThe idea is simple:when a command like cargo test, pytest, npm test, or ./gradlew test prints a lot of output, that raw log often gets pulled into the context even though only a small part is actually useful.Sift runs the command, captures the full output, and asks a nested cheaper agent call to return only a compact summary. The goal is to keep the main thread smaller and easier to work with.In one command-heavy Codex workflow I used as a baseline, this looked like roughly ~45% lower total token cost. That number is an estimate, not a benchmark claim, and it will depend a lot on the workflow. It should help most when commands produce large noisy logs. It probably does very little for short commands.Would be interested in how others handle this problem in Codex / Claude / other coding-agent setups. Comments URL: https://news.ycombinator.com/item?id=47862676 Points: 1 # Comments: 1
