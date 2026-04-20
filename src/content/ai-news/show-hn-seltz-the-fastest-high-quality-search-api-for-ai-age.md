---
title: 'Show HN: Seltz – The fastest, high quality, search API for AI agents'
description: 'Hi HN, Antonio here. Founder of Seltz.Seltz is a web search API built for AI agents. We wrote the crawler, the index, and the retrieval models ourselves, in Rust, by a team that''s spent years building'
pubDate: 2026-04-20T17:12:38
source: 'Hacker News'
sourceUrl: 'https://console.seltz.ai/login'
tags: []
---

Hi HN, Antonio here. Founder of Seltz.Seltz is a web search API built for AI agents. We wrote the crawler, the index, and the retrieval models ourselves, in Rust, by a team that's spent years building web search at scale. In our tests, queries come back in under 200ms.Efficiency was the first design principle. Search sits on the critical path: agents can't generate their first tokens or kick off the next tool call until results come back. When you run tens or hundreds of queries in parallel, every millisecond of tail latency compounds.Most search APIs for agents are wrappers around Google or Bing. If your agent already has a Google tool, a second call to a Google-wrapped API returns the same ten documents. We run our own independent index, so you get different results and different rankings.Coverage starts with US news. More verticals are coming.There's a free tier with $100 in credits at the link. I'd love feedback from anyone building agents: how does it compare to what you're using, and where does it fall over? Comments URL: https://news.ycombinator.com/item?id=47837377 Points: 4 # Comments: 1
