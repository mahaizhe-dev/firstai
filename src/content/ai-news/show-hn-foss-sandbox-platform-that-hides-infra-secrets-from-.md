---
title: 'Show HN: FOSS sandbox platform that hides infra secrets from devs and AI agents'
description: 'Hello HN. Cordium is a FOSS, self-hosted, identity-based, general-purpose sandbox platform that I''ve been working on for a long time now that is built on Kubernetes and Octelium, my main work. The key'
pubDate: 2026-06-20T13:19:20
source: 'Hacker News'
sourceUrl: 'https://github.com/octelium/cordium'
tags: []
---

Hello HN. Cordium is a FOSS, self-hosted, identity-based, general-purpose sandbox platform that I've been working on for a long time now that is built on Kubernetes and Octelium, my main work. The key difference here for Cordium, when compared to other dev environments (e.g. GitHub Codespaces) and sandbox platforms (e.g. E2B, Daytona, etc.), is that Cordium automatically provides identity-based, secretless secure access to resources/infrastructure (e.g. APIs, SSH, databases, k8s, etc.) without having to inject credentials (e.g. API keys and access tokens, SSH private keys/passwords, database passwords, mTLS private keys, etc.) into the sandbox where the upstream credential is held by the identity-aware proxy of the Octelium-protected resource outside the reach of the sandbox and inject on-the-fly by the identity-aware proxy if the user is authorized via the Octelium policies.In short, Cordium is not just an isolated execution environment that can replace remote development environments and sandbox platforms, but also equally a secure access platform to infrastructure/resources. It's basically a sandbox platform + a ZTNA/remote-access-VPN baked-in with unified identity management, L7-aware access control and visibility. Comments URL: https://news.ycombinator.com/item?id=48609062 Points: 1 # Comments: 0
