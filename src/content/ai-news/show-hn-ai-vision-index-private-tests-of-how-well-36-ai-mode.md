---
title: 'Show HN: AI Vision Index, private tests of how well 36 AI models see'
description: 'I wanted to know for my work which model is best at vision tasks (using both llms like claude and smaller models like YOLO - smaller specialist models are still not finished testing). I found that non'
pubDate: 2026-11-10T12:46:55
source: 'Hacker News'
sourceUrl: 'https://aivisionindex.com/'
tags: []
---

I wanted to know for my work which model is best at vision tasks (using both llms like claude and smaller models like YOLO - smaller specialist models are still not finished testing). I found that none of the public benchmarks were reliable: datasets were available (so they could have been used for training), and not precise enough tests.So we built our own tests, with a mix of rendered images, ai generated images, photos and videos. Every question & image pair has a specific answer, and we never publish our test data so the models can't learn them. They could learn once we've tested them, but then we will create new sets of tests.A few things that i noted:- GPT-6 Astra leads (83.7), but GPT-6.1 Sol is close (81.3) and is quite cheaper - Gemini 4 Argon & Haiku 5.5 are both very cheap and quite good! - Some tests are very easy for humans and hard for ai: counting more than 20 objects, identifying obviously ai-generated images (Argon is pretty good at that, the others are not much better than a coin flip). - Local models were tested too, Qwen3.5-9B is doing the best so far, but still lags behind the paid/API ais.Every score is dated, we also designed tests to ramp up in difficulty. We explain the method on the website. You can check which model is best at what type of test on the website & compare their price and speed too. Happy to answer questions, and if you want your own pictures tested there's a form on the site! Comments URL: https://news.ycombinator.com/item?id=50439591 Points: 1 # Comments: 1
