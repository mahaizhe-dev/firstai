---
title: 'Show HN: RS-Poker V5 The one with self learning multi-threaded async Agents'
description: 'rs-poker has been my passion project for a long time. This release is huge because it''s the first time that I know of for an open source poker bot/agent implementation to include all the state of the '
pubDate: 2026-06-09T19:48:25
source: 'Hacker News'
sourceUrl: 'https://ottercrew.group/blog/poker-v5/'
tags: []
---

rs-poker has been my passion project for a long time. This release is huge because it's the first time that I know of for an open source poker bot/agent implementation to include all the state of the art.- tokio based async exploration - rust slab allocation based tree structure for regret minimization - perfect hashing for faster hand ranking - a TUI via https://ratatui.rs/Creating your own poker bot and having them compete in an arena should be less than 100 lines of code: https://docs.rs/rs_poker/latest/rs_poker/arena/index.htmlI need more eyes on the implementation, and more attempts to make the algorithms and agents state of the art. I know I can't have found the optimal configurations and algorithms; I'd love for the open source community to prove me wrong.There's one glaring limitation that I need to fix. Right now the CFR agents can't predict their opponents hands so all regret minimization is either using the exact hand (so pretty conservative) or random (so too wide). I have some ideas here but I need more data and more discussion.direct github: https://github.com/elliottneilclark/rs-poker Comments URL: https://news.ycombinator.com/item?id=48466653 Points: 1 # Comments: 0
