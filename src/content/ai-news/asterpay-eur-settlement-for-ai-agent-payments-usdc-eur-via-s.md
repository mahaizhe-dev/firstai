---
title: 'AsterPay – EUR Settlement for AI Agent Payments (USDC → EUR via SEPA Instant)'
description: 'We built AsterPay because AI agents can earn stablecoins but can''t easily convert them to real-world currencies. Our API converts USDC/EURC to EUR via SEPA Instant in under 5 seconds. What makes it di'
pubDate: 2026-03-14T11:37:39
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47375622'
tags: []
---

We built AsterPay because AI agents can earn stablecoins but can't easily convert them to real-world currencies. Our API converts USDC/EURC to EUR via SEPA Instant in under 5 seconds. What makes it different: - Agent-native: x402 protocol (HTTP 402 pay-per-call), MCP server with 16 tools - KYA (Know Your Agent): 5-layer trust scoring (0-100) for AI agent wallets - Referenced in Google's A2A spec proposal for trust.signals[] - Free tier: trust scores, settlement estimates, identity verification Stack: Fastify, Base (L2), USDC, Bridge/Stripe for banking rails, Chainalysis for sanctions. Try it: npx @asterpay/mcp-server Docs: https://asterpay.io/docs Comments URL: https://news.ycombinator.com/item?id=47375622 Points: 2 # Comments: 1
