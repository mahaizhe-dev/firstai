---
title: 'Midjourney AI 绘画入门'
description: '学习使用 Midjourney 生成 AI 图片，包括基础命令、提示词结构和参数调节。'
pubDate: 2026-02-20
tool: 'Midjourney'
difficulty: 'beginner'
tags: ['AI绘画', '图片生成', '入门']
---

## Midjourney 简介

Midjourney 是一款基于 AI 的图片生成工具，通过文字描述即可创建各种风格的图片，适合设计师、创意工作者和普通用户。

## 准备工作

1. 注册 Discord 账号
2. 加入 Midjourney 的 Discord 服务器
3. 订阅 Midjourney 付费计划

## 基础命令

### 生成图片

在 Discord 频道中输入：

```
/imagine prompt: a cute cat sitting on a cloud, watercolor style
```

### 常用参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `--ar` | 宽高比 | `--ar 16:9` |
| `--v` | 版本 | `--v 6` |
| `--q` | 质量 | `--q 2` |
| `--s` | 风格化程度 | `--s 750` |

## 提示词结构

一个好的提示词通常包含：

1. **主题**：你想画什么
2. **风格**：油画、水彩、摄影、动漫等
3. **细节**：光线、构图、色调
4. **参数**：尺寸、版本等

### 示例

```
/imagine prompt: a futuristic city at sunset, cyberpunk style, 
neon lights, flying cars, detailed architecture, 
cinematic lighting --ar 16:9 --v 6
```

## 图片操作

生成图片后，你可以：

- **U1-U4**：放大指定图片
- **V1-V4**：基于某张图片生成变体
- **重新生成**：重新跑一次同样的提示词

## 进阶技巧

- 使用 `/describe` 命令上传图片，让 AI 反向生成提示词
- 用 `--no` 参数排除不想要的元素，如 `--no text`
- 混合两张图片使用 `/blend` 命令
