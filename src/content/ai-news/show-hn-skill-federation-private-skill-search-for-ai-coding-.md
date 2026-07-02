---
title: 'Show HN: Skill Federation – private skill search for AI coding agents'
description: 'We have been focused on AI error distribution for the past year, and in our last research paper, "Architecture of Errors" showed mathematically that an AI solution needs a finite set of interventions '
pubDate: 2026-07-02T12:58:46
source: 'Hacker News'
sourceUrl: 'https://github.com/skill-federation/skill-federation'
tags: []
---

We have been focused on AI error distribution for the past year, and in our last research paper, "Architecture of Errors" showed mathematically that an AI solution needs a finite set of interventions to perform well in a bounded patch domain (a specific application). To prove it, we ran harnessed Opus 4.6 on SkillsBench with and without wild skills (skills that you actually find on the internet) that exclude the oracle skills (the skills specifically designed for SkillsBench). That showed 17.5% -> 22.8% (~30% relative lift) as expected.To run the test, we have created a skill search engine for AI agent-native use - not for humans. Agents imagine the perfect set of skills that would be useful for their planned task and Skill Federation fetches them. The engine uses current SOTA tricks such as key word enrichment and reranking and reproduces SOTA numbers on SkillRet.The skills come from internal storage that is pre scanned to the best effort with Cisco and Nvidia security scanners.The search is free. We personally use it for our projects and now sharing this with the rest of the humans and their agents. Comments URL: https://news.ycombinator.com/item?id=48760839 Points: 1 # Comments: 0
