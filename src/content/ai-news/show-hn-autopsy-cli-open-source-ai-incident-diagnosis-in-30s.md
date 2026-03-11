---
title: 'Show HN: Autopsy CLI – Open-source AI incident diagnosis in 30s'
description: 'Hi HN,I''ve been building Autopsy, an open-source CLI tool to solve a problem I hate: manually digging through CloudWatch logs during a 3 AM page.It pulls your CloudWatch logs and GitHub deploys, passe'
pubDate: 2026-03-11T14:30:47
source: 'Hacker News'
sourceUrl: 'https://news.ycombinator.com/item?id=47336048'
tags: []
---

Hi HN,I've been building Autopsy, an open-source CLI tool to solve a problem I hate: manually digging through CloudWatch logs during a 3 AM page.It pulls your CloudWatch logs and GitHub deploys, passes them to an LLM, and returns a structured root cause analysis in your terminal in about 30 seconds.The early version worked, but the diagnosis vanished the moment you closed your terminal. I just shipped v0.2.2 to make it actually fit into an SRE/DevOps workflow:Local History: Every run now saves automatically to a local SQLite DB. You can search, browse, and export past incidents (autopsy history list).Instant Post-Mortems: Passing --postmortem generates a full incident report in Markdown, including a timeline, evidence, and checkbox action items.Slack Integration: Passing --slack pushes the diagnosis directly to your incident channel via webhook.You can chain them: autopsy diagnose --postmortem --slackA big priority here is privacy. It’s built with Python, runs locally, and your logs never leave your machine (aside from the direct payload you choose to send to the LLM).GitHub: https://github.com/zeelapatel/autopsy PyPI: pip install autopsy-cliI'd love for you to try it out. I'm especially looking for feedback on the LLM's diagnosis accuracy across different types of stack traces and log formats. Happy to answer any questions! Comments URL: https://news.ycombinator.com/item?id=47336048 Points: 1 # Comments: 0
