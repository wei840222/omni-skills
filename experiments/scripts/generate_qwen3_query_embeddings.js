#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { createStore } = require('/home/wei/Documents/Gitea/wei840222/qmd/dist/index.js');

async function main() {
  const rootDir = path.resolve(__dirname, '..');
  const dbPath = path.join(rootDir, '.qmd', 'index.sqlite');
  const configDir = path.join(rootDir, '.qmd');
  const queriesPath = path.join(rootDir, 'datasets', 'benchmark_queries.json');
  const outPath = path.join(rootDir, 'datasets', 'query_embeddings.json');

  const queries = JSON.parse(fs.readFileSync(queriesPath, 'utf-8'));
  console.log(`[*] Loaded ${queries.length} queries from ${queriesPath}`);

  const store = await createStore({ dbPath, configDir });
  const llm = store.internal.llm;

  console.log('[*] Embedding queries with local Qwen3-Embedding...');
  const embeddings = [];

  const startTime = Date.now();
  for (let i = 0; i < queries.length; i++) {
    const qText = queries[i].natural_prompt;
    const res = await llm.embed(qText);
    const embArray = res.embedding ? Array.from(res.embedding) : Array.from(res);
    embeddings.push(embArray);
    if ((i + 1) % 50 === 0 || i === queries.length - 1) {
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
      console.log(`  [${i + 1}/${queries.length}] Embedded in ${elapsed}s (Dim: ${embArray.length})`);
    }
  }

  fs.writeFileSync(outPath, JSON.stringify(embeddings), 'utf-8');
  console.log(`[✓] Successfully saved ${embeddings.length} embeddings (1024-dim) to ${outPath}`);

  await store.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
