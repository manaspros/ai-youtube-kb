export const meta = {
  name: 'aie-extract',
  description: 'Haiku agents turn AI Engineer talk transcripts into structured, timestamped notes (one agent per video)',
  whenToUse: 'After transcripts land in /path/to/ai-youtube-kb/data/wf/text; args = array of video ids from `aie.py wf-prep-extract`',
  phases: [{ title: 'Extract', detail: 'one Haiku agent per video', model: 'haiku' }],
}

const ROOT = '/path/to/ai-youtube-kb'
const CATS = ['software-factory','pr-code-review','coding-agents','testing-verification','context-engineering',
  'skills-self-improvement','memory','rag-retrieval','evals','observability','mcp-and-tools','multi-agent',
  'agent-architecture','inference-serving','training-finetuning-rl','voice-multimodal','security-guardrails',
  'governance-compliance','sandboxing-execution','infra-cost-scaling','product-ux','enterprise-adoption',
  'data-engineering','models-research']
const S = {type: 'string'}
const NOTE = {
  type: 'object',
  required: ['id','one_line','summary','speakers','orgs','format','topics','tags','key_ideas','techniques',
             'tools','numbers','hot_takes','relevance','quality','depth'],
  properties: {
    id: S,
    one_line: {type: 'string', description: 'what the talk is about + main takeaway, <=30 words'},
    summary: {type: 'string', description: '5-8 plain sentences'},
    speakers: {type: 'array', items: S}, orgs: {type: 'array', items: S},
    format: {type: 'string', enum: ['talk','workshop','panel','keynote','interview','demo','other']},
    topics: {type: 'array', items: {type: 'string', enum: CATS}, minItems: 1, maxItems: 4},
    tags: {type: 'array', items: S},
    key_ideas: {type: 'array', items: {type: 'object', required: ['idea','detail','t'],
      properties: {idea: S, detail: S, t: {type: 'string', description: 'm:ss or h:mm:ss'}}}},
    techniques: {type: 'array', items: {type: 'object', required: ['name','how','when'],
      properties: {name: S, how: S, when: S}}},
    tools: {type: 'array', items: S},
    numbers: {type: 'array', items: {type: 'object', required: ['claim','t'], properties: {claim: S, t: S}}},
    hot_takes: {type: 'array', items: S},
    relevance: {type: 'array', items: {type: 'object', required: ['project','score','why','action'],
      properties: {project: {type: 'string', enum: ['agentos','gateway','prosharness','general']},
                   score: {type: 'integer', minimum: 0, maximum: 3}, why: S, action: S}}},
    quality: {type: 'integer', minimum: 1, maximum: 5},
    depth: {type: 'string', enum: ['intro','practitioner','deep']},
  },
}

const ids = args
log(`extracting ${ids.length} videos with Haiku`)
phase('Extract')
const results = await pipeline(ids, (id) => agent(
  `You write research notes for one AI Engineer conference video.\n` +
  `1. Read ${ROOT}/data/wf/extract_system.md — the rules, category list and project profile. Follow them exactly.\n` +
  `2. Read ${ROOT}/data/wf/text/${id}.txt with the Read tool (pass allow_large: true; if it is still cut off, read the rest with offset).\n` +
  `3. Return the notes. Set id="${id}". Do not write any files.`,
  {label: `extract:${id}`, phase: 'Extract', model: 'haiku', schema: NOTE}))
const ok = results.filter(Boolean)
log(`done: ${ok.length}/${ids.length}`)
return {ok: ok.length, failed: ids.filter((id, i) => !results[i])}
