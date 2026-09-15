---
title: 'Ask HN: The amount of AI bot traffic is out control?'
description: 'We host a web app which has around 50,000 statically generated public pages, and the amount of bot traffic is insane. Facebook’s crawler requested the same pages over 3 million times in 2 days, and we'
pubDate: 2026-09-14T23:36:01
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=49705724'
tags: []
---

We host a web app which has around 50,000 statically generated public pages, and the amount of bot traffic is insane. Facebook’s crawler requested the same pages over 3 million times in 2 days, and we’ve used Vercel and Cloudflare to block as much as possible but it’s not working. The AI scrapers are routing requests through residential proxies, and even after putting our entire app behind an Auth gate with cloudflare turnstile they’re creating accounts to get access to data that’s meant for humans to read / use. I’ve never seen anything like it before, our hosting costs are up like crazy, and besides all of this, I can’t trust anything I read or see on this web anymore. As a last resort we’ll try switching to hcaptcha tomorrow instead of turnstile which appears to be more difficult but this is all so depressing to me. Want to hear if anyone else is experiencing this, there’s no way I’m the only here who is struggling with sophisticated bots? Comments URL: https://news.ycombinator.com/item?id=49705724 Points: 5 # Comments: 2
