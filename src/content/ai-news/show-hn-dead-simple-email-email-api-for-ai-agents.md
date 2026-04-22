---
title: 'Show HN: Dead Simple Email – Email API for AI Agents'
description: 'We built this after running into the same wall everyone hits: Gmail suspends bot accounts within days, SES is outbound-only with no inbox or threading, and the only purpose-built option jumps from $20'
pubDate: 2026-04-22T17:48:44
source: 'Hacker News'
sourceUrl: 'https://deadsimple.email/'
tags: []
---

We built this after running into the same wall everyone hits: Gmail suspends bot accounts within days, SES is outbound-only with no inbox or threading, and the only purpose-built option jumps from $20/mo to $200/mo with nothing in between. Dead Simple Email gives AI agents their own email addresses via API. No OAuth, no human in the loop. Each inbox gets a real address, send/receive, webhook on inbound mail, and full conversation threading. Infrastructure is our own. KumoMTA for outbound delivery, Dovecot for IMAP, dedicated mail servers. Not a reseller sitting on top of SES. MCP server is included, so agents built on Claude, ChatGPT, or any MCP-compatible LLM connect natively without writing integration code. Pricing: 5 inboxes free, 100 inboxes for $29/mo, 500 for $99/mo. Docs: https://deadsimple.email/docs.html API reference: https://deadsimple.email/api-reference.html#description/rate... Happy to answer questions about deliverability, infrastructure, or how it compares to the alternatives. Comments URL: https://news.ycombinator.com/item?id=47866879 Points: 2 # Comments: 0
