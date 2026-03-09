import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://mahaizhe-dev.github.io',
  base: '/firstai',
  output: 'static',
  build: {
    assets: '_assets',
  },
  vite: {
    build: {
      cssMinify: true,
    },
  },
});
