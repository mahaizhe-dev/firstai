---
title: 'Show HN: Lumbox – Email infrastructure for AI agents (lumbox.co)'
description: 'Been building agents that need to sign up for services, verify email addresses, and extract OTPs. The missing piece in most agent stacks is a real email identity per agent.Lumbox gives each agent its '
pubDate: 2026-03-18T07:20:29
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47422578'
tags: []
---

Been building agents that need to sign up for services, verify email addresses, and extract OTPs. The missing piece in most agent stacks is a real email identity per agent.Lumbox gives each agent its own inbox. The main thing that makes it different from rolling your own:GET /otp is a long-poll endpoint that blocks until the OTP arrives. Your agent just calls it and waits. No polling loop, no webhook setup, no extra infra.Also ships with Steel Browser integration so the full signup/verify flow is a single skill call: skill_signup_with_email handles navigate, fill form, submit, wait for OTP, enter OTP.There is also a credential vault where agents never see passwords - they are typed into fields directly without being exposed in the conversation or logs.We just rebranded from AgentMailr to Lumbox after a trademark conflict with AgentMail (YC-backed). Their $6M raise is good validation the problem is real.Free tier: 3 inboxes, 500 emails received/month. lumbox.coHappy to answer questions about the architecture or the long-poll approach. Comments URL: https://news.ycombinator.com/item?id=47422578 Points: 1 # Comments: 0
