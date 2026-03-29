---
title: 'Ask HN: How are you keeping AI coding agents from burning money?'
description: 'My agents retry a bit more than it should, and there goes my bill up in the sky. I tried figuring out what is causing this but none of the tools helped much.and the worse thing for me is that everythi'
pubDate: 2026-03-29T00:22:20
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47559293'
tags: []
---

My agents retry a bit more than it should, and there goes my bill up in the sky. I tried figuring out what is causing this but none of the tools helped much.and the worse thing for me is that everything shows up as aggregate usage. Total tokens, total cost, maybe per model.So I ended up hacking together a thin layer in front of OpenAI where every request is forced to carry some context (agent, task, user, team), and then just logging and calculating cost per call and putting some basic limits on top so you can actually block something if it starts going off the rails. It’s very barebones, but even just seeing “this agent + this task = this cost” was a big relief.It uses your own OpenAI key, so it’s not doing anything magical on the execution side, just observing and enforcing.I want to know you guys are dealing with this right now. Are you just watching aggregate usage and trusting it, or have you built something to break it down per agent / task?If useful, here is the rough version I’m using : https://authority.bhaviavelayudhan.com/ Comments URL: https://news.ycombinator.com/item?id=47559293 Points: 3 # Comments: 8
