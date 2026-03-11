---
title: 'Show HN: ClawDiary – Audit log and human approval gate for AI agents (Claw, MCP'
description: 'ClawDiary is an audit diary and guard for AI agents. I use Cursor a lot and wanted something that (a) logs what the agent does and (b) blocks dangerous actions until I approve them in Telegram.What it'
pubDate: 2026-03-09T14:15:08
source: 'Hacker News'
sourceUrl: 'https://github.com/jetywolf/claw-diary'
tags: []
---

ClawDiary is an audit diary and guard for AI agents. I use Cursor a lot and wanted something that (a) logs what the agent does and (b) blocks dangerous actions until I approve them in Telegram.What it does: - Audit: agents POST to /v1/audit after each action; writes go to D1 async so the agent isn’t blocked. - Guard: before risky ops (rm, drop table, execute_bash, transfer, etc.) the agent calls /v1/guard. Request is stored and the call blocks until you approve or reject in Telegram (or by updating DB). Green-light actions return immediately. - Diary, daily digest (cron), and a minimal timeline UI so I can see what happened.Stack: Cloudflare Worker, Hono, D1, Durable Objects (for holding the guard request until approval). Cursor integration is via a .cursor/rules rule that calls the API; MCP-capable agents can use the tool described at /mcp.json.Repo: https://github.com/jetywolf/claw-diary Live API/docs: https://api.clawdiary.org/docsHappy to answer questions or take feedback. Comments URL: https://news.ycombinator.com/item?id=47309377 Points: 2 # Comments: 0
