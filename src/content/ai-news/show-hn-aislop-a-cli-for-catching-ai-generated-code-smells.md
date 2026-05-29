---
title: 'Show HN: AISlop, a CLI for catching AI generated code smells'
description: 'Hi, I’m Kenny, I’ve been building aislop. I starting working on this after using Claude Code, codex and opencode several times and noticing some slops. They aren’t syntax and passes most tests, they a'
pubDate: 2026-05-29T13:37:38
source: 'Hacker News'
sourceUrl: 'https://github.com/scanaislop/aislop'
tags: []
---

Hi, I’m Kenny, I’ve been building aislop. I starting working on this after using Claude Code, codex and opencode several times and noticing some slops. They aren’t syntax and passes most tests, they are patterns like empty catch blocks, useless comments, duplicated helpers, dead code and many more. So I built a tool to scan and check for these patterns and wired it into hooks so after each tool call, the agent checks for the slops.You can try it out with npx aislop scan.It’s all local and no code is transferred. Thank you. Comments URL: https://news.ycombinator.com/item?id=48322956 Points: 48 # Comments: 35
