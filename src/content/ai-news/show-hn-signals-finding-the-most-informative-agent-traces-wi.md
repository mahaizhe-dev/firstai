---
title: 'Show HN: Signals – finding the most informative agent traces without LLM judges'
description: 'Hey HNSalman, Shuguang and Adil here from Katanemo Labs (a DigitalOcean company).Wanted to introduce our latest research on agentic systems called Signals. If you''ve been building agents, you''ve proba'
pubDate: 2026-04-05T02:27:25
source: 'Hacker News'
sourceUrl: 'https://arxiv.org/abs/2604.00356'
tags: []
---

Hey HNSalman, Shuguang and Adil here from Katanemo Labs (a DigitalOcean company).Wanted to introduce our latest research on agentic systems called Signals. If you've been building agents, you've probably noticed that there are far too many agent traces/trajectories to review one by one, and using humans or extra LLM calls to inspect all of them gets expensive really fast. The paper proposes a lightweight way to compute structured “signals” from live agent interactions so you can surface the trajectories most worth looking at, without changing the agent’s online behavior. Computing Signals doesn't require a GPU.Signals are grouped into a simple taxonomy across interaction, execution, and environment patterns, including things like misalignment, stagnation, disengagement, failure, looping, and exhaustion. In an annotation study on τ-bench, signal-based sampling reached an 82% informativeness rate versus 54% for random sampling, which translated to a 1.52x efficiency gain per informative trajectory.Paper: arXiv 2604.00356. Project where Signals are already implemented: https://github.com/katanemo/planoHappy to answer questions on the taxonomy, implementation details, or where this breaks down. Comments URL: https://news.ycombinator.com/item?id=47645594 Points: 3 # Comments: 0
