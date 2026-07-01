---
title: '0/6 major aerospace documentation portals are AI Agent-ready'
description: 'I spent some time building AeroScore, a scoring engine that evaluates how well major documentation portals support AI agents. In short, none of the 6 that I evaluated in this first batch are sufficien'
pubDate: 2026-07-01T19:15:22
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48751798'
tags: []
---

I spent some time building AeroScore, a scoring engine that evaluates how well major documentation portals support AI agents. In short, none of the 6 that I evaluated in this first batch are sufficiently prepared.The methodology and criteria are based on the AFDocs Spec (an open-source checklist for agent-ready documentation) and one specific extension for PDF-heaviness since aerospace as a field places so much importance on PDFs. Each site gets scored 0-100 across criteria like llms.txt presence, robots.txt, and many others that can be found both on the AFDocs repo and at the aeroscore webpage.Key Findings: -0/6 have an llms.txt -0/6 support url variants -the best score was ICAO with a 69/100The fact that major aerospace documentation portals are not AI agent ready yet is important because it means the field is not being fully efficient. AI agents allow the analysis of data across deep documentation portals to occur in fractions of the expected time, and this has revolutionized many fields. The lack of this in aerospace means a loss of productivity.The leaderboard is live at: https://aeroscore.vercel.appThe AFDocs repo is at: https://github.com/agent-ecosystem/afdocsI'm an incoming undergraduate aerospace engineering student interested in how AI is and can be implemented in my field. This is v1 of aeroscore, it's pretty rough and I'd appreciate feedback on the methodology greatly. In future versions, I'll be scoring more sites with a refurbished rubric. Comments URL: https://news.ycombinator.com/item?id=48751798 Points: 1 # Comments: 0
