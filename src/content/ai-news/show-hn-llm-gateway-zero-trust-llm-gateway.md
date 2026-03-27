---
title: 'Show HN: LLM-Gateway – Zero-Trust LLM Gateway'
description: 'I built an OpenAI-compatible LLM gateway that routes requests to OpenAI, Anthropic, Ollama, vLLM, llama-server, SGLang... anything that speaks /v1/chat/completions. Single Go binary, one YAML config f'
pubDate: 2026-03-27T14:22:43
source: 'Hacker News'
sourceUrl: 'https://github.com/openziti/llm-gateway'
tags: []
---

I built an OpenAI-compatible LLM gateway that routes requests to OpenAI, Anthropic, Ollama, vLLM, llama-server, SGLang... anything that speaks /v1/chat/completions. Single Go binary, one YAML config file, no infrastructure.It does the things you'd expect from this kind of gateway... semantic routing via a three-layer cascade (keyword heuristics, embedding similarity, LLM classifier) that picks the best model when clients omit the model field, weighted round-robin load balancing across local inference servers with health checks and failover.The part I think is most interesting is the network layer. The gateway and backends communicate over zrok/OpenZiti overlay networks... reach a GPU box behind NAT, expose the gateway to clients, put components anywhere with internet connectivity behind firewalls... no port forwarding, no VPN. Zero-trust in both directions. Most LLM proxies solve the API translation problem. This one also solves the network problem.Apache 2.0. https://github.com/openziti/llm-gatewayI work for NetFoundry, which sponsors the OpenZiti project this is built on. Comments URL: https://news.ycombinator.com/item?id=47542999 Points: 3 # Comments: 0
