---
title: 'Agent.json – robots.txt for AI agent-to-website communication'
description: 'I built agent.json, an open protocol that makes websites message-addressable by AI agents. The problem: when an AI agent needs to request a refund or book an appointment, there''s no standard way. No A'
pubDate: 2026-03-13T13:42:57
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47364358'
tags: []
---

I built agent.json, an open protocol that makes websites message-addressable by AI agents. The problem: when an AI agent needs to request a refund or book an appointment, there's no standard way. No API, and the contact form wasn't designed for software. agent.json adds three endpoints to any website: 1. GET /.well-known/agent.json - discovery (actions, schemas, auth) 2. POST /.agent/inbox - send a message 3. GET /.agent/inbox/:id - poll for a response Actions have JSON Schema parameters so agents know exactly what to send. Responses support sync, polling, or HMAC-signed webhook callbacks. It's platform-agnostic - implement in Express, Django, Rails, Go, anything. The repo includes a reference implementation on Cloudflare Workers with AI classification, email routing, and a dashboard. Docs: https://agent-json.com Would love feedback on the protocol design. Comments URL: https://news.ycombinator.com/item?id=47364358 Points: 2 # Comments: 1
