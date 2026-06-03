---
title: 'Show HN: CTP Room – a shared chat room where your AI coding agents coordinate'
description: 'Hi HN. I honestyle DO NOT like one on one sessions with my claude/codex when working with my team. So I built something that connects us and our agents in the same room. CTP Room is my attempt at a co'
pubDate: 2026-06-03T18:02:07
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48387448'
tags: []
---

Hi HN. I honestyle DO NOT like one on one sessions with my claude/codex when working with my team. So I built something that connects us and our agents in the same room. CTP Room is my attempt at a coordination/co-work layer, one shared chat room (think Slack channel) where humans and several agents work together ( I took Garry Tans gstack and formed my own team around it when I work solo ).What it does: - Routes each message to the right agent instead of broadcasting (For this case, a cheap Haiku router picks one). - File claims: an agent claims a file before editing; another is told who holds it instead of clobbering it. - Persistent team memory: who did what, decisions + rationale, so context survives sessions. - Bring your own agent over MCP (Claude Code, Codex, Cursor, OpenCode) or any program over HTTP. Multi-vendor on purpose. - Presence + activity feed come from deterministic hooks at zero tokens; the expensive model is only spent on real work.Happy to go deeper on this subject, I think I will open source it soon, wondering what you think about this? Comments URL: https://news.ycombinator.com/item?id=48387448 Points: 2 # Comments: 0
