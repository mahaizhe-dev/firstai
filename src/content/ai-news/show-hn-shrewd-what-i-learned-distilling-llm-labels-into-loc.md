---
title: 'Show HN: Shrewd – what I learned distilling LLM labels into local classifiers'
description: 'General purpose LLMs, and classifiers like Jev, are nice and easy to use right away. That makes the pain of labelling data and creating specialized models for simple tasks not seem worth it, but for a'
pubDate: 2026-09-22T20:00:46
source: 'Hacker News'
sourceUrl: 'https://github.com/sshah03/shrewd'
tags: []
---

General purpose LLMs, and classifiers like Jev, are nice and easy to use right away. That makes the pain of labelling data and creating specialized models for simple tasks not seem worth it, but for a project I am working on, I needed to create a large number of specialized models that could run efficiently on-device.This project started as a way for me to test if GEPA could get frontier LLMs to generate better labels for me. I had mixed results. It works better on weaker models than on true frontier models, but there were definitely some gains.I decided I'd rerun some of the flows on public datasets that are often used for these comparisons and post it, as I'm curious 1) what results others get with it, and 2) what ideas others have for doing a better job of this.I've tried to document everything I could thoroughly, but always happy to chat.Some things I want to try next: 1) Generating synthetic questions to train on, not just the labels, likely by using multiple models to validate agreement on whether it's a worthwhile question to add to the set 2) Support RAG in the labelling flow by simply pointing to some docs or a corpus and have the rest be automatedI couldn't think of a good project name so shrewd is just: shrew->something small, and d-> distillation. I know distillation is a bit of a loaded word right now, but this is more just a labelling task, and into very small single-purpose models, so it is hopefully not an issue. Comments URL: https://news.ycombinator.com/item?id=49807276 Points: 3 # Comments: 0
