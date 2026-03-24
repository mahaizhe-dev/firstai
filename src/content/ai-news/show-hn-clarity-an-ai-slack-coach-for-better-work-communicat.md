---
title: 'Show HN: Clarity – An AI Slack coach for better work communication'
description: 'Clarity is a Slack bot to serve as a private communication coach, directly addressing the biggest hurdle in remote work: miscommunication. By using LLMs, Clarity analyzes your messages after you hit s'
pubDate: 2026-03-24T18:55:09
source: 'Hacker News'
sourceUrl: 'https://clarity.rocktangle.com/'
tags: []
---

Clarity is a Slack bot to serve as a private communication coach, directly addressing the biggest hurdle in remote work: miscommunication. By using LLMs, Clarity analyzes your messages after you hit send, offering instant auto-edits for issues like tone and clarity.The core technical hurdle was evaluating "good communication," which is inherently subjective and couldn't rely on standard test sets. To overcome this, we designed a sophisticated, multi-LLM evaluation pipeline. One powerful LLM synthesized the initial flagging test set, a second acted as a judge for precision and recall, and a third continuously auto-tuned the prompt for the flagger LLM, resulting in high confidence in our system's accuracy. Furthermore, we built a dedicated agent to simulate Clarity operating in various synthetic workspaces—featuring diverse industries, sectors, and personas in conflict-prone situations—to further validate its performance.We intentionally launched Clarity as an individual-focused product to lower the barrier to entry, with the strategic goal of establishing usage before transitioning to a team-based model (M1). We are now seeking community feedback on the product before expanding our reach. Comments URL: https://news.ycombinator.com/item?id=47507454 Points: 2 # Comments: 0
