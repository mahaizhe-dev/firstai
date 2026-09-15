---
title: 'Show HN: Jinfer – AI inference engine for the JVM. AI in a jar'
description: 'Hi HN, Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and TTS. No Python runtime, no ONNX, '
pubDate: 2026-09-15T06:42:32
source: 'Hacker News'
sourceUrl: 'https://qxotic.ai/'
tags: []
---

Hi HN, Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and TTS. No Python runtime, no ONNX, no Docker containers, no sidecar process, no IPC. Finally, AI in a jar.The stack underneath is built for the JVM rather than bolted onto it: toknroll: pure-Java tokenizers, zero dependencies gguf / safetensors: read and write llama.cpp and HuggingFace model formats jam: quantized matmul kernels, competitive with llama.cpp on CPU jota: Tensor API targeting Java, C, CUDA, HIP, Metal, OpenCL, and Mojo It ships with integrations for Spring AI and LangChain4j, and is compatible with GraalVM Native Image for low-overhead, self-contained binaries with millisecond startup.This is an early release (CPU only): I'd especially like feedback on the API surface.Site: https://qxotic.ai Repo: https://github.com/qxoticai/qxotic Comments URL: https://news.ycombinator.com/item?id=49708628 Points: 2 # Comments: 0
