---
title: 'Show HN: AgentMailr – dedicated email inboxes for AI agents'
description: 'I kept running into the same problem while building AI agents: every agent that needs email ends up sharing my personal inbox or a single company domain. That breaks attribution, creates deliverabilit'
pubDate: 2026-03-15T11:29:37
source: 'Hacker News'
sourceUrl: 'https://www.agentmailr.com/'
tags: []
---

I kept running into the same problem while building AI agents: every agent that needs email ends up sharing my personal inbox or a single company domain. That breaks attribution, creates deliverability risk, and makes it impossible to test sender identities per agent.So I built AgentMailr. You call an API to create an inbox, your agent gets a unique email address, and replies route back to that specific agent. Works for both inbound (OTP parsing, reply routing) and outbound (cold email, notifications).Bring your own domain is supported so emails come from your domain, not ours. REST API and MCP server are live. Node/Python SDKs are in progress.Happy to answer questions about the architecture or how I'm handling multi-agent routing. Comments URL: https://news.ycombinator.com/item?id=47386367 Points: 5 # Comments: 1
