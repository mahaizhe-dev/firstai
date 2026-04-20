---
title: 'Show HN: LLM-Rosetta - Translate LLM API Calls Across OpenAI, Anthropic, Gemini'
description: 'I built this after getting tired of maintaining one-off adapters between OpenAI, Anthropic, and Gemini APIs in the same project.The idea is to translate through a shared intermediate representation in'
pubDate: 2026-04-20T07:05:33
source: 'Hacker News'
sourceUrl: 'https://github.com/Oaklight/llm-rosetta'
tags: []
---

I built this after getting tired of maintaining one-off adapters between OpenAI, Anthropic, and Gemini APIs in the same project.The idea is to translate through a shared intermediate representation instead of writing every provider pair separately. So instead of OpenAI->Anthropic, OpenAI->Gemini, Anthropic->Gemini, etc., each provider just maps to/from the IR.This is not a unified client like LiteLLM. It's a translator/proxy: give it an OpenAI-style request and it can produce the Anthropic/Gemini equivalent, including streaming, tool calls, and multimodal inputs.It's open source, and there's also a gateway mode if you want to run it as a proxy in front of multiple providers.Would especially love feedback on where translation breaks down or gets too lossy across providers.Docs: https://llm-rosetta.readthedocs.io Paper/design notes: https://arxiv.org/abs/2604.09360 Comments URL: https://news.ycombinator.com/item?id=47831189 Points: 2 # Comments: 0
