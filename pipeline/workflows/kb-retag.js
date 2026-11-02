export const meta = {
  name: 'kb-retag',
  description: 'Haiku agents re-assign categories to existing notes after the taxonomy grows (batches of ~25 notes per agent)',
  whenToUse: 'After adding categories to context/categories.md: `aie.py wf-prep-retag` prints {batches, cats} = args; afterwards `aie.py wf-import-retag --latest`',
  phases: [{ title: 'Retag', detail: 'one Haiku agent per batch', model: 'haiku' }],
}

const ROOT = '/path/to/ai-youtube-kb'
const { batches, cats } = args
const jobs = Array.from({ length: batches }, (_, i) =>
  ({ file: `${ROOT}/data/wf/retag/batch_${String(i).padStart(3, '0')}.md` }))
const OUT = { type: 'object', required: ['retags'], properties: { retags: { type: 'array', items: {
  type: 'object', required: ['id', 'topics'], properties: {
    id: { type: 'string' },
    topics: { type: 'array', items: { type: 'string', enum: cats }, minItems: 1, maxItems: 4 } } } } } }

phase('Retag')
log(`${jobs.length} batches of ~25 notes`)
const res = await pipeline(jobs, (j, _, i) => agent(
  `Re-tag video notes with the category taxonomy, which recently gained new categories.\n` +
  `1. Read ${ROOT}/data/wf/retag/categories.md — every category slug with what it covers.\n` +
  `2. Read ${j.file} — about 25 videos; each starts with "### \`<id>\`" and lists current topics, tags, one-liner, techniques, tools.\n` +
  `3. For EVERY video return 1-4 topics, most central first. Keep current topics that still fit; add a new category ` +
  `when the video is substantially about it (e.g. a talk mainly about Claude Code features → claude-code; cutting ` +
  `token spend → token-cost-efficiency; running models on own GPUs → local-ai). Do not add a category for a passing mention.\n` +
  `Return one entry for EVERY video in the file, with its id copied exactly from the "### \`<id>\`" heading. Do not write files.`,
  { label: `retag:${i}`, phase: 'Retag', model: 'haiku', schema: OUT }))
const ok = res.filter(Boolean)
const failed = jobs.filter((j, i) => !res[i]).map(j => j.file)
log(`retagged ${ok.reduce((a, r) => a + r.retags.length, 0)} notes${failed.length ? '; failed batches: ' + failed.join(', ') : ''}`)
return { batches: ok.length, failed }
