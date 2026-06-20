---
title: 'Changes that cut our LLM pipeline costs more than model-switching did'
description: 'I have been building multiple LLM systems and for our Organization biggest cost savings weren''t from prompt-wordsmithing or model switchings. Sharing useful to anyone watching their token bill :1) JSO'
pubDate: 2026-06-20T13:05:31
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=48608978'
tags: []
---

I have been building multiple LLM systems and for our Organization biggest cost savings weren't from prompt-wordsmithing or model switchings. Sharing useful to anyone watching their token bill :1) JSON → TOON for structured output: JSON was not made for LLMs. well you can implement your own verison that fits for your needs that reduce tokens usage but what worked for us was TOON. TOON cut output our tokens by ~30% same information, way less syntax tax.2) Full markdown/HTML → condensed markdown: Using markdown for writing your prompts, getting intermediate results or communication between your Agents eats a lot of tokens. We swithced to condesed markdown and short system prompts that replicate Caveman. this alone cut just on input token costs ~50% on calls that pass prior context forward which can be implemented between Agent Calls.3) Long Do/Don't instruction lists → 2-3 multi-shot examples: Counterintuitive one - replacing a large lists of DO's and Don'ts for agents rules don't help. rather couple of concrete examples that convers major and all cases actually improved output quality more reliably and it's usually fewer tokens once the instruction list gets long enough to cover real edge cases.I have seen most people on this sub reddit talk about using open-source or cheaper models. Like we were spending thousands of dollar's but this all changes alone helped reduce cost by 60%.edit: Open to Discussion, anyone whether something similar would help their setup. Comments URL: https://news.ycombinator.com/item?id=48608978 Points: 2 # Comments: 0
