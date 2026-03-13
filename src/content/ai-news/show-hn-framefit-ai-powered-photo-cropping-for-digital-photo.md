---
title: 'Show HN: FrameFit – AI-powered photo cropping for digital photo frames'
description: 'I built this because I was tired of manually cropping family photos for my digital photo frame. Every frame has a different aspect ratio and when you just resize, you end up cutting people''s heads off'
pubDate: 2026-03-13T18:38:00
source: 'Hacker News'
sourceUrl: 'https://framefit.photo'
tags: []
---

I built this because I was tired of manually cropping family photos for my digital photo frame. Every frame has a different aspect ratio and when you just resize, you end up cutting people's heads off or losing the important parts of the photo. FrameFit uses Claude to analyze the photo, detect faces and key subjects, then crop intelligently for whatever aspect ratio your frame needs. Upload a photo, pick your frame dimensions, get a crop that actually keeps the important stuff in frame. Stack: Next.js 16, Claude API for image analysis, Stripe for payments, Supabase Postgres, deployed on Vercel. Free tier gives you 5 crops per day. Pro is €4.99/month if you need more. Would love to hear feedback on the crop quality. The hardest part was getting the AI to understand composition, not just face detection. Sometimes you want the landscape in the background, not just a tight face crop. Comments URL: https://news.ycombinator.com/item?id=47367973 Points: 2 # Comments: 0
