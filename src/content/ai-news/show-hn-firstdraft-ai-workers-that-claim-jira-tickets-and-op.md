---
title: 'Show HN: FirstDraft – AI workers that claim Jira tickets and open PRs'
description: 'I’ve been spending a lot of time with Codex at work like many people, and found myself doing the same thing over and over:- Pick a Jira ticket - Start an agent - Explain the task - Wait for it to fini'
pubDate: 2026-06-04T19:04:46
source: 'Hacker News'
sourceUrl: 'https://firstdraft.run'
tags: []
---

I’ve been spending a lot of time with Codex at work like many people, and found myself doing the same thing over and over:- Pick a Jira ticket - Start an agent - Explain the task - Wait for it to finish - Open a PR - RepeatSo I built FirstDraft.A worker runs on a machine that already has access to your repositories, build tools, credentials, and anything else it needs. It watches a Jira board, claims a ticket, runs Claude Code or Codex locally, pushes a branch, and opens a draft PR.The goal was to push through some of those smaller bug tickets and features that could be done without me having to pick them up myself.What’s been interesting is that once I got the basics working, I started using FirstDraft to build FirstDraft. A lot of the features in the current version were implemented by workers picking up Jira tickets and opening PRs.It’s still early and very much an experiment, but it’s been a fun one. Comments URL: https://news.ycombinator.com/item?id=48403166 Points: 2 # Comments: 0
