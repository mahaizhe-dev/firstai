import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const aiNews = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/ai-news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    source: z.string(),
    sourceUrl: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

const aiTutorials = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/ai-tutorials' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tool: z.string(),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']).default('beginner'),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

const worldNews = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/world-news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    source: z.string(),
    sourceUrl: z.string().url().optional(),
    region: z.string().optional(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

const historyNews = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/history-news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    source: z.string(),
    sourceUrl: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

export const collections = { 'ai-news': aiNews, 'ai-tutorials': aiTutorials, 'world-news': worldNews, 'history-news': historyNews };
