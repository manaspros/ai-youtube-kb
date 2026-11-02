export const meta = {
  name: 'kb-update',
  description: 'Haiku-only incremental update of the YouTube KB: new videos on every tracked channel → Whisper transcripts → notes → index → guides/insights "What\'s new" → trends',
  whenToUse: 'Routine refresh (e.g. weekly). args optional: {since: "20260518", channel: "aie", limit: 60}. Every agent is Haiku.',
  phases: [
    { title: 'Prep', detail: 'Haiku runs aie.py update-prep: list channels, Whisper new videos, stage text', model: 'haiku' },
    { title: 'Extract', detail: 'kb-extract.js: one Haiku agent per new video', model: 'haiku' },
    { title: 'Import', detail: 'Haiku runs wf-import + index + wf-prep-synth', model: 'haiku' },
    { title: 'Guides', detail: 'kb-guides.js mode=update: Haiku writers + verifiers + trends', model: 'haiku' },
  ],
}

const ROOT = '/path/to/ai-youtube-kb'
const A = args || {}
const since = A.since || '20260518'
const PREP = { type: 'object', required: ['queue', 'today'], properties: {
  queue: { type: 'integer', description: 'the "queue" number update-prep printed' }, today: { type: 'string' },
  queueDir: { type: 'string', description: 'the "queueDir" value update-prep printed' },
  notes: { type: 'string', description: 'errors or warnings worth surfacing, else ""' } } }
const DONE = { type: 'object', required: ['ok', 'output'], properties: {
  ok: { type: 'boolean' }, output: { type: 'string', description: 'last lines of each command' } } }

let prep = A.queue != null ? A : null
if (!prep) {
  phase('Prep')
  const flags = `--since ${since}` + (A.channel ? ` --channel ${A.channel}` : '') + (A.limit ? ` --limit ${A.limit}` : '')
  prep = await agent(
    `Run this with the Bash tool (timeout 600000 ms; Whisper transcribes new videos on the GPU, so it can take minutes):\n` +
    `cd ${ROOT} && ./pipeline/aie.py update-prep ${flags}\n` +
    `If it times out, run it again (finished transcripts are kept). Its last line is JSON like {"queue": 12, "queueDir": "queue_update", "today": "YYYY-MM-DD"}; ` +
    `return those values. Do not edit files.`,
    { label: 'update-prep', phase: 'Prep', model: 'haiku', schema: PREP })
  if (!prep) return { error: 'update-prep failed' }
  if (prep.notes) log(prep.notes)
}
const today = prep.today || A.today
if (!prep.queue) { log('no new videos'); return { new: 0 } }
log(`${prep.queue} new videos since ${since}`)

phase('Extract')
// taxonomy omitted: kb-extract falls back to its built-in list, which mirrors context/categories.md
const ex = await workflow({ scriptPath: `${ROOT}/pipeline/workflows/kb-extract.js` },
                          { queue: prep.queue, queueDir: prep.queueDir || 'queue_update', ...(A.cats ? { cats: A.cats, formats: A.formats } : {}) })
const got = ex.notes.map(n => n.id)
if (!got.length) return { new: prep.queue, extracted: 0, failed: ex.failed }

phase('Import')
const csv = got.join(',')
const imp = await agent(
  `Run with the Bash tool, one command at a time, from ${ROOT}; stop at the first failure:\n` +
  `1. ./pipeline/aie.py wf-import --latest --ids ${csv}\n2. ./pipeline/aie.py index\n` +
  `3. ./pipeline/aie.py wf-prep-synth --since ${since} --ids ${csv} > /dev/null\n` +
  `Return ok=true only if all three exit 0, plus the last lines each printed.`,
  { label: 'import+index', phase: 'Import', model: 'haiku', schema: DONE })
if (!imp || !imp.ok) return { error: 'import failed', output: imp && imp.output, extracted: got }
log(imp.output.split('\n').filter(l => /imported|indexed/.test(l)).join(' · '))

// route new notes to docs: every category they carry, and each project they scored >= 2 for
// (mirrors what `wf-prep-synth --ids` just wrote to data/wf/synth/)
const byCat = {}, byProj = {}
for (const n of ex.notes) {
  for (const t of n.topics) (byCat[t] = byCat[t] || []).push(n.id)
  for (const p of n.relevance) if (p !== 'general') (byProj[p] = byProj[p] || []).push(n.id)
}
const jobs = [
  ...Object.entries(byProj).map(([name, ids]) => ({ kind: 'project', name, n: ids.length, ids })),
  ...Object.entries(byCat).map(([name, ids]) => ({ kind: 'category', name, n: ids.length, ids })),
]

phase('Guides')
const g = await workflow({ scriptPath: `${ROOT}/pipeline/workflows/kb-guides.js` }, { jobs, mode: 'update', since, today })
return { new: prep.queue, extracted: got.length, failed: ex.failed, docs: g && g.docs.length, trends: g && g.trends }
