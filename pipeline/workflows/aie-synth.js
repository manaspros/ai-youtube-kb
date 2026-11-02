export const meta = {
  name: 'aie-synth',
  description: 'Sonnet agents write category guides + project insight reviews from AI Engineer talk notes, verify citations, then a trends overview',
  whenToUse: 'After `aie.py wf-prep-synth --since YYYYMMDD` wrote data/wf/synth/*; args = {jobs, since} from that command',
  phases: [
    { title: 'Synthesize', detail: 'Sonnet: one guide per category, one review per project', model: 'sonnet' },
    { title: 'Verify', detail: 'check every cited video supports the claim; fix or flag', model: 'sonnet' },
    { title: 'Trends', detail: 'Sonnet: what changed over the window + what to do now', model: 'sonnet' },
  ],
}

const ROOT = '/path/to/ai-youtube-kb'
const PROJECT_DOCS = {
  agentos: ['<local path>', '<local path>',
            '<local path>'],
  prosharness: ['<local path>', '<local path>'],
  gateway: [],
}
const OUT = {type: 'object', required: ['path', 'cited_ids', 'headline'], properties: {
  path: {type: 'string'},
  cited_ids: {type: 'array', items: {type: 'string'}},
  headline: {type: 'string', description: '3-5 sentences: the most important takeaways of the doc'},
}}
const VERDICT = {type: 'object', required: ['checked', 'fixed', 'notes'], properties: {
  checked: {type: 'integer'}, fixed: {type: 'integer'}, notes: {type: 'string'},
}}
const { jobs, since } = args
const RULES = 'Paraphrase; never paste transcript passages or long quotes. Cite videos as `video_id`. Plain, short sentences.'

function synthPrompt(j) {
  if (j.kind === 'category') {
    return `Write the field guide for the "${j.name}" category of the AI Engineer channel KB (talks since ${since}).\n` +
      `1. Read ${ROOT}/data/wf/synth/topic_system.md — the required sections and the project profile.\n` +
      `2. Read ${ROOT}/data/wf/synth/cat_${j.name}.md (allow_large: true) — compact notes for ${j.n} talks.\n` +
      `3. When a claim needs detail, open ${ROOT}/kb/videos/<id>.md (timestamped notes). Open 5-10 of the best ones.\n` +
      `4. Write ${ROOT}/kb/guides/${j.name}.md starting with "# Guide: ${j.name}" and an italic line ` +
      `"Synthesized by Sonnet from ${j.n} talks since ${since}." ${RULES}\n` +
      `Return the path, every video id you cited, and a headline.`
  }
  const docs = PROJECT_DOCS[j.name].map(p => `   - ${p}`).join('\n')
  return `Review our "${j.name}" project against what AI Engineer talks (since ${since}) found.\n` +
    `1. Read ${ROOT}/data/wf/synth/insight_system.md — required sections + project profile.\n` +
    (docs ? `2. Read the project's own docs so you know what is actually built vs planned:\n${docs}\n` : '2. (No repo docs for this project; rely on the profile.)\n') +
    `3. Read ${ROOT}/data/wf/synth/proj_${j.name}.md (allow_large: true) — notes for ${j.n} relevant talks.\n` +
    `4. Before ranking a gap, open the cited ${ROOT}/kb/videos/<id>.md to confirm the talk says it.\n` +
    `5. Write ${ROOT}/kb/insights/${j.name}.md starting with "# Insights: ${j.name}" and an italic line ` +
    `"Synthesized by Sonnet from ${j.n} talks since ${since}." Do not claim we lack something the docs show is built. ${RULES}\n` +
    `Return the path, every video id you cited, and a headline.`
}

function verifyPrompt(r) {
  return `Fact-check ${r.path}. It cites AI Engineer talks as \`video_id\`; each talk's notes are in ${ROOT}/kb/videos/<id>.md.\n` +
    `For every concrete claim tied to a citation (numbers, techniques, "X found Y"), open that video's notes and check the claim is supported. ` +
    `Try to refute each one. If a claim is wrong or unsupported, fix it in place with Edit (correct it, re-cite, or delete it). ` +
    `Remove citations of ids that have no notes file. Do not add new content. Return how many claims you checked and fixed.`
}

phase('Synthesize')
log(`${jobs.length} docs: ${jobs.filter(j => j.kind === 'project').map(j => j.name).join(', ')} + categories`)
const done = await pipeline(jobs,
  (j) => agent(synthPrompt(j), {label: `${j.kind}:${j.name}`, phase: 'Synthesize', model: 'sonnet', schema: OUT}),
  // project reviews drive decisions, so each gets a Sonnet skeptic; guides get a cheaper Haiku citation pass
  (r, j) => agent(verifyPrompt(r), {label: `verify:${j.name}`, phase: 'Verify', schema: VERDICT,
                                    model: j.kind === 'project' ? 'sonnet' : 'haiku'})
    .then(v => ({...r, job: j, verify: v})))
const ok = done.filter(Boolean)
log(`synthesized + verified ${ok.length}/${jobs.length}`)

phase('Trends')
const digest = ok.map(r => `- ${r.job.kind} ${r.job.name} (${r.job.n} talks, ${r.path}): ${r.headline}`).join('\n')
const trends = await agent(
  `Write ${ROOT}/kb/trends.md: "What changed in AI engineering since ${since}" for an engineer who builds agent infra.\n` +
  `Headlines of every guide and project review:\n${digest}\n\n` +
  `Open the guides/reviews you need (paths above) and ${ROOT}/kb/latest.md. Sections:\n` +
  `## The 10 shifts that matter (dated, each citing guides + \`video_id\`s)\n## Where the field disagrees\n` +
  `## Do this now — AgentOS / ProsHarness / gateway (ranked; link the insight docs)\n## If you watch only 10 talks\n` +
  `${RULES} Start the file with "# Trends since ${since}".`,
  {label: 'trends', phase: 'Trends', model: 'sonnet', schema: OUT})
return {docs: ok.map(r => ({path: r.path, verify: r.verify})), failed: jobs.filter((j, i) => !done[i]).map(j => j.name),
        trends: trends && trends.path}
