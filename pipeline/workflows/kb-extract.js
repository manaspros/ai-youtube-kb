export const meta = {
  name: 'kb-extract',
  description: 'Haiku agents turn YouTube transcripts (any tracked channel) into structured, timestamped notes, one agent per video',
  whenToUse: 'After `aie.py wf-prep-extract [--channel ..]` staged data/wf/queue/q*.txt. args = {queue: N, queueDir?, offset?, count?, cats, formats} (or {ids: [...]}, or a plain id array)',
  phases: [{ title: 'Extract', detail: 'one Haiku agent per video', model: 'haiku' }],
}

const ROOT = '/path/to/ai-youtube-kb'
const A = Array.isArray(args) ? { ids: args } : (args || {})
// queue mode: item i reads data/wf/queue/q<i>.txt; the id comes from its "Video id:" header line
const offset = A.offset || 0
const qdir = A.queueDir || 'queue'
const count = A.queue != null ? Math.min(A.count || A.queue, A.queue - offset) : 0
const items = A.queue != null
  ? Array.from({ length: Math.max(0, count) }, (_, k) => ({ q: `q${String(offset + k).padStart(4, '0')}` }))
  : (A.ids || []).map(id => ({ id }))
// fallbacks only matter for a bare id array; wf-prep-extract always sends the live taxonomy from context/categories.md
const CATS = A.cats || ['software-factory','pr-code-review','coding-agents','testing-verification','context-engineering',
  'skills-self-improvement','memory','rag-retrieval','evals','observability','mcp-and-tools','multi-agent',
  'agent-architecture','inference-serving','training-finetuning-rl','voice-multimodal','security-guardrails',
  'governance-compliance','sandboxing-execution','infra-cost-scaling','product-ux','enterprise-adoption',
  'data-engineering','models-research','claude-code','token-cost-efficiency','local-ai','vibe-coding-app-building','dev-tools']
const FORMATS = A.formats || ['talk','workshop','panel','keynote','interview','demo','tutorial','news','review','other']
const S = { type: 'string' }
const NOTE = {
  type: 'object',
  required: ['id','one_line','summary','speakers','orgs','format','topics','tags','key_ideas','techniques',
             'tools','numbers','hot_takes','relevance','quality','depth'],
  properties: {
    id: S,
    one_line: { type: 'string', description: 'what the video is about + main takeaway, <=30 words' },
    summary: { type: 'string', description: '5-8 plain sentences' },
    speakers: { type: 'array', items: S }, orgs: { type: 'array', items: S },
    format: { type: 'string', enum: FORMATS },
    topics: { type: 'array', items: { type: 'string', enum: CATS }, minItems: 1, maxItems: 4 },
    tags: { type: 'array', items: S },
    key_ideas: { type: 'array', items: { type: 'object', required: ['idea','detail','t'],
      properties: { idea: S, detail: S, t: { type: 'string', description: 'm:ss or h:mm:ss' } } } },
    techniques: { type: 'array', items: { type: 'object', required: ['name','how','when'],
      properties: { name: S, how: S, when: S } } },
    tools: { type: 'array', items: S },
    numbers: { type: 'array', items: { type: 'object', required: ['claim','t'], properties: { claim: S, t: S } } },
    hot_takes: { type: 'array', items: S },
    relevance: { type: 'array', items: { type: 'object', required: ['project','score','why','action'],
      properties: { project: { type: 'string', enum: ['agentos','gateway','prosharness','general'] },
                    score: { type: 'integer', minimum: 0, maximum: 3 }, why: S, action: S } } },
    quality: { type: 'integer', minimum: 1, maximum: 5 },
    depth: { type: 'string', enum: ['intro','practitioner','deep'] },
  },
}

log(`extracting ${items.length} videos with Haiku`)
phase('Extract')
const results = await pipeline(items, (it) => {
  const file = it.id ? `${ROOT}/data/wf/text/${it.id}.txt` : `${ROOT}/data/wf/${qdir}/${it.q}.txt`
  const idRule = it.id ? `Set id="${it.id}".` : `Set id to the value on the file's first line ("Video id: ..."), copied exactly.`
  return agent(
    `You write research notes for one YouTube video.\n` +
    `1. Read ${ROOT}/data/wf/extract_system.md — the rules, category list and project profile. Follow them exactly.\n` +
    `2. Read ${file} with the Read tool (pass allow_large: true; if it is still cut off, read the rest with offset). ` +
    `Its header names the video id, channel, title, date and length.\n` +
    `3. Return the notes. ${idRule} Do not write any files.`,
    { label: `extract:${it.id || it.q}`, phase: 'Extract', model: 'haiku', schema: NOTE })
})
const notes = results.filter(Boolean)
const failed = items.filter((it, i) => !results[i]).map(it => it.id || it.q)
if (failed.length) log(`failed (a re-run of wf-prep-extract re-queues them): ${failed.join(', ')}`)
log(`done: ${notes.length}/${items.length}`)
// compact view for callers (kb-update) that route notes to guides; full notes stay in the journal for wf-import
return { ok: notes.length, failed,
         notes: notes.map(n => ({ id: n.id, topics: n.topics, quality: n.quality,
                                  relevance: (n.relevance || []).filter(r => r.score >= 2).map(r => r.project) })) }
