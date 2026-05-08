---
title: 'AniTroves – An anime database with a custom LLM-based discovery hub'
description: 'I’ve always felt that traditional anime databases rely too heavily on rigid tag-based searches. If you’re looking for a specific "vibe" or a very niche trope that isn''t a primary tag, you usually end '
pubDate: 2026-05-08T02:00:08
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48057592'
tags: []
---

I’ve always felt that traditional anime databases rely too heavily on rigid tag-based searches. If you’re looking for a specific "vibe" or a very niche trope that isn't a primary tag, you usually end up scrolling through pages of irrelevant results.I built AniTroves (https://anitroves.com) to experiment with a more conversational, LLM-driven approach to series discovery.The Tech Behind the Hub:LLM Integration: Instead of a generic API wrapper, I've been working on a custom hub (https://anitroves.com/ai-hub/) that uses specialized models to understand series lore and character archetypes for roleplay and discovery.Anipick Engine: This is the logic layer that maps natural language queries to our database entries.Technical Transparency: I’ve implemented a structured llms.txt (https://anitroves.com/llms.txt) to provide a machine-readable source of truth for other crawlers and AI models.I’m currently the technical administrator and I'm handling the SEO and server scaling (managed on Hostinger) myself. I’ve recently been troubleshooting some 504 gateway issues during traffic spikes, so the site is a work in progress!I'd love to get the community's feedback on the UX of the AI Hub and how I can better structure my data for AI-readiness.Questions for HN:Does the conversational discovery feel more useful than standard tag filtering to you?How are you handling llms.txt or robots.txt for your own AI-adjacent projects in 2026? Comments URL: https://news.ycombinator.com/item?id=48057592 Points: 2 # Comments: 0
