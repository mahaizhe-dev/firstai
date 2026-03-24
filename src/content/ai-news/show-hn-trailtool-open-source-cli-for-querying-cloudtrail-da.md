---
title: 'Show HN: TrailTool – open-source CLI for querying CloudTrail data with AI agents'
description: 'I''ve been working on AWS security for years and querying CloudTrail has always been a huge pain - getting data about like "what did this role actually use in the last 30 days?" means either writing cu'
pubDate: 2026-03-24T18:59:40
source: 'Hacker News'
sourceUrl: 'https://github.com/engseclabs/trailtool'
tags: []
---

I've been working on AWS security for years and querying CloudTrail has always been a huge pain - getting data about like "what did this role actually use in the last 30 days?" means either writing custom queries and result parsing code or getting vague data from built-in tools like Access Analyzer.TrailTool's core idea is to pre-aggregate CloudTrail events at ingest time into entity relationships — People, Sessions, Roles, Services, Resources — so queries are DynamoDB reads rather than log scans. The CLI talks directly to your DynamoDB tables using standard AWS credentials, no API layer needed.The four workflows in the post (ClickOps detection, least-privilege policy generation, AccessDenied remediation, break-glass validation) all came from things I was actually doing manually. The session transcripts are real Claude Code runs using the tool.Wondering if this feels useful to folks, or if there are other CloudTrail questions that could be pre-computed this way to accomplish common tasks. Comments URL: https://news.ycombinator.com/item?id=47507510 Points: 2 # Comments: 0
