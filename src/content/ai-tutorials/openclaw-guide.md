---
title: 'OpenClaw（龙虾）使用指南：搭建你的 AI 数字员工'
description: '学习如何安装和使用 OpenClaw（龙虾），配置多种 AI 模型，对接企业微信/飞书/钉钉，让 AI 主动帮你处理邮件、日历和文档。'
pubDate: 2026-03-09
tool: 'OpenClaw'
difficulty: 'beginner'
tags: ['OpenClaw', 'AI Agent', '自动化']
---

## 什么是 OpenClaw

OpenClaw（社区昵称"龙虾"）是 2026 年最火的开源 AI Agent 框架，GitHub 星标超过 15 万。它不是普通的聊天机器人，而是真正能执行任务的「数字员工」——可以接管你的键鼠、调用系统 API，主动帮你处理邮件、管理日历、整理文档。

## 核心能力

- **办公自动化**：自动整理收件箱、分类邮件、定时提醒
- **日历管理**：同步多平台日程，实时提醒会议
- **文档处理**：PDF/Word/PPT 转 Markdown，自动摘要归档
- **知识管理**：打通 Obsidian/Notion，一句话自动归档、打标签、排版
- **全渠道通信**：支持企业微信、飞书、钉钉、Telegram、Discord 等 20+ 平台
- **主动执行**：能主动监控系统、发送提醒、执行定时任务

## 快速安装

### 方式一：一行命令安装（推荐）

支持 macOS、Windows、Linux，会自动安装 Node.js 等所有依赖：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### 方式二：npm 全局安装

```bash
npm i -g openclaw
openclaw onboard
```

### 方式三：源码构建

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw && pnpm install && pnpm run build
pnpm run openclaw onboard
```

### 方式四：云端部署

不想折腾本地环境，可以一键部署到云服务器：
- **阿里云**：适合长期在线运行和后续扩容
- **腾讯云**：适合快速跑通验证

### 方式五：桌面客户端（Beta）

从 [GitHub Releases](https://github.com/openclaw/openclaw/releases/latest) 下载桌面版，支持 macOS / Windows / Linux。

## 配置 AI 模型

OpenClaw 支持接入多种大模型，在设置中配置 API Key 即可：

| 模型 | 推荐场景 | 获取方式 |
|------|----------|----------|
| 豆包/火山 | 通用任务，低延迟高性价比 | volcengine.com |
| 阿里云百炼 | 多模型可选，Coding Plan 有优惠 | aliyun.com |
| 智谱 GLM | 长文档理解，复杂逻辑推理 | bigmodel.cn |
| DeepSeek | 中文理解强，性价比极高 | platform.deepseek.com |

## 对接通讯平台

OpenClaw 最强大的能力之一是全渠道通信。以企业微信为例：

1. 在企业微信管理后台创建自建应用
2. 获取 CorpID、AgentID、Secret
3. 在 OpenClaw 配置文件中填入凭证
4. 启用消息回调和事件订阅

配置完成后，你可以直接在企业微信中和 AI 助手对话，让它帮你执行各种任务。

同样的方式也适用于飞书、钉钉、微信公众号等平台。

## 实用场景

### 邮件助手

```
帮我查看今天的未读邮件，标记紧急邮件并总结要点
```

### 会议管理

```
把明天下午的产品评审会提前30分钟，并通知所有参会人
```

### 文档整理

```
把桌面上的 PDF 报告转成 Markdown，提取关键数据并归档到 Obsidian
```

### 定时监控

```
每天早上9点给我发送今日待办事项和天气预报
```

## 与 LobeChat 的区别

| 对比项 | OpenClaw（龙虾） | LobeChat |
|--------|-----------------|----------|
| 定位 | AI Agent，能执行任务 | AI 聊天界面 |
| 操作能力 | 可接管键鼠、调用系统 API | 仅对话 |
| 平台集成 | 20+ 通讯平台 | 无 |
| 主动性 | 能主动执行定时任务 | 被动回复 |
| 本地运行 | 本地优先 | 本地或云端 |

## 注意事项

> OpenClaw 能操控你的电脑，请仅在可信环境中使用，谨慎授予敏感权限。

- 首次使用建议先在测试环境验证
- 定期更新到最新版本以获得安全修复
- 加入微信交流群可以获得社区帮助和最新使用技巧
