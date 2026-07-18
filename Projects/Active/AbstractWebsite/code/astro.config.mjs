import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://abstractwebsite.example.com',
  prefetch: true,
  compressHTML: true,
});