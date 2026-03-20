---
title: 'Ask HN: How do you programmatically evaluate if an LLM sounds "too AI"?'
description: 'Hi HN,I’m currently building Aaptics, a tool designed to help founders draft content. The biggest engineering challenge hasn''t been the infrastructure, but getting the underlying models to stop soundi'
pubDate: 2026-03-20T04:38:34
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47450556'
tags: []
---

Hi HN,I’m currently building Aaptics, a tool designed to help founders draft content. The biggest engineering challenge hasn't been the infrastructure, but getting the underlying models to stop sounding like a corporate robot (e.g., stopping it from using words like "delve", "testament", or "in today's fast-paced landscape").Right now, my pipeline uses a custom RAG setup that ingests a user's past writing, combined with heavy negative-prompting and few-shot examples. However, the model still occasionally slips into that recognizable "ChatGPT tone."For those of you building AI applications, how are you quantitatively evaluating the "humanness" of your outputs?Are you using LLM-as-a-judge frameworks?Relying on specific temperature/top_p tweaking?Or hardcoding penalizations for certain n-grams?I'm aiming to finalize this pipeline before our mid-April launch and would appreciate any insights from folks who have solved this in production. aaptics.in/waitlist Comments URL: https://news.ycombinator.com/item?id=47450556 Points: 1 # Comments: 0
