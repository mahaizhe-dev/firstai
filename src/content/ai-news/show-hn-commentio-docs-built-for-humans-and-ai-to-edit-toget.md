---
title: 'Show HN: Comment.io – Docs built for humans and AI to edit together'
description: 'I built a collaborative markdown editor designed for humans and AI agents to work on the same document.The key thing: agents already know how to edit files with old\_string/new\_string. Comment.io use'
pubDate: 2026-03-17T15:43:04
source: 'Hacker News'
sourceUrl: 'https://comment.io'
tags: []
---

I built a collaborative markdown editor designed for humans and AI agents to work on the same document.The key thing: agents already know how to edit files with old\_string/new\_string. Comment.io uses the exact same pattern as its agent API. You can tell your agent "make a doc at comment.io" or "add notes to comment.io/my-doc-url" and it figures out how to use it immediately — no SDK, no copying instructions, just curl.Every line tracks authorship — human, AI, or both — so you always know where each idea came from.Each document gets a fully isolated environment. Encrypted at rest and in transit. No login, no accounts — share a link and start writing.It runs on Cloudflare Workers + Durable Objects with Yjs CRDTs, which keeps it simple enough that I can make it free forever.I built this because I kept watching my agents (and teammates) get confused trying to collaborate on docs. The fix was making docs work the way agents already think — like files.Live at comment.io. Happy to answer questions here or on Discord (https://discord.gg/khfSzSDh>). Comments URL: https://news.ycombinator.com/item?id=47414259 Points: 1 # Comments: 0
