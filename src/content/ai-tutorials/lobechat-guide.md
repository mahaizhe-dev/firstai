---
title: 'LobeChat 使用指南：搭建你的私人 AI 助手'
description: '学习如何部署和使用 LobeChat（龙虾），配置多种 AI 模型，打造个性化的聊天界面和知识库。'
pubDate: 2026-03-09
tool: 'LobeChat'
difficulty: 'beginner'
tags: ['LobeChat', '私有部署', 'AI 助手']
---

## 什么是 LobeChat

LobeChat（社区昵称"龙虾"）是一个开源的 AI 聊天框架，支持接入多种大语言模型（OpenAI、DeepSeek、Claude、Gemini 等），提供美观的界面和丰富的功能。你可以把它部署为自己的私人 AI 助手。

## 核心特性

- **多模型支持**：一个界面切换 OpenAI、DeepSeek、Claude、Gemini 等模型
- **插件系统**：搜索、画图、代码执行等插件扩展能力
- **知识库**：上传文档，让 AI 基于你的资料回答问题
- **角色预设**：创建不同用途的 AI 角色（翻译、编程、写作等）
- **本地部署**：数据完全掌控在自己手中

## 快速上手

### 方式一：Vercel 一键部署（最简单）

1. 打开 [github.com/lobehub/lobe-chat](https://github.com/lobehub/lobe-chat)
2. 点击 "Deploy with Vercel" 按钮
3. 登录 Vercel 账号，确认部署
4. 部署完成后，在设置中填入你的 AI API Key

### 方式二：Docker 本地部署

```bash
docker run -d -p 3210:3210 \
  -e OPENAI_API_KEY=sk-xxxx \
  lobehub/lobe-chat
```

启动后访问 `http://localhost:3210` 即可使用。

### 方式三：桌面客户端

从 [github.com/lobehub/lobe-chat/releases](https://github.com/lobehub/lobe-chat/releases) 下载对应系统的安装包，安装后直接使用。

## 配置 API Key

进入设置页面，可以配置多个 AI 提供商的 Key：

| 提供商 | 获取地址 | 推荐模型 |
|--------|----------|----------|
| DeepSeek | platform.deepseek.com | deepseek-chat |
| OpenAI | platform.openai.com | gpt-4o |
| Claude | console.anthropic.com | claude-3.5-sonnet |
| Gemini | aistudio.google.com | gemini-pro |

## 创建 AI 角色

1. 点击左侧 "发现" 进入角色市场
2. 选择现成的角色模板，或点击 "+" 创建自定义角色
3. 编写系统提示词（System Prompt）定义角色行为
4. 选择使用的模型和参数

### 角色示例：代码审查专家

```
你是一位经验丰富的高级工程师。
当用户提交代码时，你需要：
1. 指出潜在的 bug 和性能问题
2. 提出改进建议
3. 评估代码的可读性和可维护性
请用中文回复，并给出具体的代码修改示例。
```

## 知识库功能

1. 进入"知识库"页面
2. 创建新的知识库
3. 上传 PDF、Markdown、TXT 等文档
4. 在对话中选择关联的知识库
5. AI 会基于你上传的资料来回答问题

## 实用技巧

- **快捷键**：`/` 可快速搜索角色，`Ctrl+N` 新建对话
- **话题分支**：长按消息可以从任意位置创建分支对话
- **导出对话**：支持导出为 Markdown、图片等格式
- **移动端**：网页版完美适配手机浏览器，也可添加到主屏幕
