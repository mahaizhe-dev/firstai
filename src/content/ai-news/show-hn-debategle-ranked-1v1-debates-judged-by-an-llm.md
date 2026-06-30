---
title: 'Show HN: Debategle – ranked 1v1 debates judged by an LLM'
description: 'I built Debategle, a platform for live 1v1 debates. You get matched with a random opponent (ranked matching is based on topics you’re interested in, casual matches are just open rooms), you each argue'
pubDate: 2026-06-30T13:08:53
source: 'Hacker News'
sourceUrl: 'https://debategle.com/'
tags: []
---

I built Debategle, a platform for live 1v1 debates. You get matched with a random opponent (ranked matching is based on topics you’re interested in, casual matches are just open rooms), you each argue your side, and an LLM judges who made the better case.Stack: FastAPI backend, Clerk for auth, Elo-style rating system for ranked matches. The obvious objection is LLM-as-judge reliability, I don’t think it’s perfect, but I’ve found it’s decent at scoring argument structure and rebuttals rather than just rewarding confident-sounding text. Curious what people think breaks it, I’m sure there are ways to game the judging that I haven’t found yet. Comments URL: https://news.ycombinator.com/item?id=48732235 Points: 1 # Comments: 0
