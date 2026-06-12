---
title: 'Show HN: AI Chat App on Durable Streams and Tanstack DB'
description: 'I built an AI chat app that uses Durable Streams from ElectricSQL as both the storage format and transport medium. It has the very nice property that tokens are stored durably as they are steamed back'
pubDate: 2026-06-12T17:18:58
source: 'Hacker News'
sourceUrl: 'https://oss.chat/tour'
tags: []
---

I built an AI chat app that uses Durable Streams from ElectricSQL as both the storage format and transport medium. It has the very nice property that tokens are stored durably as they are steamed back from the LLM provider, and then streamed to the frontend for a smooth user experience.The frontend uses Tanstack DBs differential dataflow implementation to tie together meta data from Postgres with the chat streams in the Durable Stream.Made a detailed explainer of all the components. Comments URL: https://news.ycombinator.com/item?id=48506809 Points: 2 # Comments: 0
