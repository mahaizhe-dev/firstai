---
title: 'Show HN: X402 integrations for an AI-agent data API, checked in a clean room'
description: 'I run Blockchain IQ. We sell some crypto data to software agents per request over x402 (HTTP 402, USDC on Base, no account or API key). In October we paid for integrations: 22 were submitted and we ch'
pubDate: 2026-10-28T16:50:10
source: 'Hacker News'
sourceUrl: 'https://www.blockchainiq.co/blog/x402-integrations-from-the-build-bounty'
tags: []
---

I run Blockchain IQ. We sell some crypto data to software agents per request over x402 (HTTP 402, USDC on Base, no account or API key). In October we paid for integrations: 22 were submitted and we checked each one by matching its on-chain payment to our purchase log and running it in a clean temporary folder with a throwaway wallet. Twenty passed; the post lists all of them with the exact commits we ran. To try the API: `curl -i https://www.blockchainiq.co/api/x402/v1/brief` returns the 402 with the price ($0.01), and a wallet's first call is free. Questions about how we checked the code or what failed are welcome. Comments URL: https://news.ycombinator.com/item?id=50276639 Points: 1 # Comments: 0
