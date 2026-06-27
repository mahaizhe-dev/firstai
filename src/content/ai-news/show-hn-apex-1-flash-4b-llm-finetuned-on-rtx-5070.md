---
title: 'Show HN: Apex-1-flash, 4B LLM finetuned on RTX 5070'
description: 'The goal was to create a highly efficient, small-scale model that can perform reasoning tasks while remaining lightweight enough to run easily on consumer hardware. Technical Stack: Base: Qwen3:4B Tra'
pubDate: 2026-06-27T15:07:51
source: 'Hacker News'
sourceUrl: 'https://huggingface.co/OrbitAIEU/Apex-1-flash'
tags: []
---

The goal was to create a highly efficient, small-scale model that can perform reasoning tasks while remaining lightweight enough to run easily on consumer hardware. Technical Stack: Base: Qwen3:4B Training: Fine-tuned using Unsloth for memory efficiency, which allowed me to run the process smoothly on an RTX 5070. Stack: Built with cu128, PyTorch, and Hugging Face Transformers. Dataset: Trained on Raymond-dev-546730/Open-CoT-Reasoning-Mini to improve Chain-of-Thought (CoT) capabilities. Comments URL: https://news.ycombinator.com/item?id=48698923 Points: 2 # Comments: 0
