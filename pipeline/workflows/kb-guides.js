export const meta = {
  name: 'kb-guides',
  description: 'Haiku agents write or update category guides + project insight docs from video notes, fact-check citations, refresh trends.md',
  whenToUse: 'args = {jobs, mode, since, today} with jobs from `aie.py wf-prep-synth`. mode "creators": add a "From creator channels" section (new guides for new categories). mode "update": add new videos to a dated "What\'s new" section.',
  phases: [
    { title: 'Write', detail: 'one Haiku agent per guide / insight doc', model: 'haiku' },
    { title: 'Verify', detail: 'Haiku citation fact-check of the edited section', model: 'haiku' },
    { title: 'Trends', detail: 'Haiku refreshes kb/trends.md', model: 'haiku' },
  ],
}

const ROOT = '/path/to/ai-youtube-kb'
const { jobs, mode, since, today } = args
const CREATORS = 'Kai Explains, AI LABS, Better Stack'
const OUT = { type: 'object', required: ['path', 'section', 'cited_ids', 'headline'], properties: {
  path: { type: 'string' },
  section: { type: 'string', description: 'heading of the section you wrote, or "whole doc" if you created the file' },
  cited_ids: { type: 'array', items: { type: 'string' } },
  headline: { type: 'string', description: '2-4 sentences: the most important things you added' },
} }
const VERDICT = { type: 'object', required: ['checked', 'fixed', 'notes'], properties: {
  checked: { type: 'integer' }, fixed: { type: 'integer' }, notes: { type: 'string' } } }
const RULES = 'Paraphrase; never paste transcript passages or long quotes. Cite videos as `video_id`, only ids that ' +
  'appear in the input notes. Plain, short sentences; no filler. Say when a claim comes from a single creator video ' +
  'or a sponsored segment. Edit with the Edit tool (Write only for a file that does not exist yet).'

function docPath(j) { return `${ROOT}/kb/${j.kind === 'project' ? 'insights' : 'guides'}/${j.name}.md` }
function notesFile(j) { return `${ROOT}/data/wf/synth/${j.kind === 'project' ? 'proj' : 'cat'}_${j.name}.md` }

function writePrompt(j) {
  const path = docPath(j), src = notesFile(j)
  const read = `Read ${ROOT}/data/wf/synth/${j.kind === 'project' ? 'insight' : 'topic'}_system.md (required sections + our project profile), ` +
    `then ${src} (allow_large: true): compact notes for ${j.n} videos. When a claim needs detail, open ${ROOT}/kb/videos/<id>.md ` +
    `(timestamped notes); open the 4-8 best ones.`
  const create = `If ${path} does not exist, create it: first line "# ${j.kind === 'project' ? 'Insights' : 'Guide'}: ${j.name}", ` +
    `then an italic line "Synthesized ${today} by Haiku from ${j.n} videos. Open a video: \`kb/videos/<id>.md\`.", ` +
    `then every section the system file lists (keep sections short when evidence is thin), and report section "whole doc".`
  if (mode === 'creators') {
    const body = j.kind === 'project'
      ? `### Ideas and tools to try (ranked, each: what, why for this project, \`video_id\`)\n### Claims to treat with caution`
      : `### Practical playbook (numbered; concrete steps, commands, settings, prompts; cite each)\n` +
        `### Tools creators recommend (tool — what for — \`video_id\`)\n` +
        `### Where creators agree or clash with the conference talks\n### Watch first (3-6 \`video_id\` — why)`
    return `Add what the creator channels (${CREATORS}) teach about "${j.name}" to our knowledge base.\n${read}\n` +
      `${create}\nOtherwise the file already holds a guide built from AI Engineer conference talks: keep it, and add ` +
      `(or replace, if it exists) one section "## From creator channels (${CREATORS})" placed just before ` +
      `"## Watch first" or "## Reading list" (append at the end if neither exists). Sub-sections:\n${body}\n` +
      `Do not change any other section. ${RULES}\nReturn the path, the section heading, every cited id and a headline.`
  }
  return `New videos landed for "${j.name}" (update of ${today}; ${j.n} new videos: ${(j.ids || []).join(', ')}).\n${read}\n` +
    `${create}\nOtherwise keep the doc and maintain a section "## What's new" placed right after the italic line under the title ` +
    `(create it if missing). Add one bullet per new video worth knowing, newest first: ` +
    `"- **YYYY-MM-DD** · Channel — finding (\`video_id\`)". Keep at most 25 bullets; drop the oldest. Skip videos with ` +
    `quality <= 2 unless they report a fact (release, number). If a new video changes a consensus point or a number elsewhere ` +
    `in the doc, update that sentence in place and cite it; otherwise leave the other sections alone. ${RULES}\n` +
    `Return the path, the section heading ("What's new" or "whole doc"), every cited id and a headline.`
}

function verifyPrompt(r) {
  const scope = r.section === 'whole doc' ? 'the whole file' : `only the section "${r.section}"`
  return `Fact-check ${scope} of ${r.path}. It cites videos as \`video_id\`; each one's notes are in ${ROOT}/kb/videos/<id>.md.\n` +
    `For every concrete claim tied to a citation (numbers, commands, tools, "X found Y"), open that video's notes and check ` +
    `the claim is supported. Try to refute each one. If a claim is wrong or unsupported, fix it in place with Edit (correct it, ` +
    `re-cite, or delete it). Remove citations of ids that have no notes file. Do not add new content and do not touch other ` +
    `sections. Return how many claims you checked and fixed.`
}

phase('Write')
log(`${mode}: ${jobs.length} docs (${jobs.filter(j => j.kind === 'project').map(j => j.name).join(', ') || 'no projects'} + categories)`)
const done = await pipeline(jobs,
  (j) => agent(writePrompt(j), { label: `${j.kind}:${j.name}`, phase: 'Write', model: 'haiku', schema: OUT }),
  (r, j) => agent(verifyPrompt(r), { label: `verify:${j.name}`, phase: 'Verify', model: 'haiku', schema: VERDICT })
    .then(v => ({ ...r, job: j, verify: v })))
const ok = done.filter(Boolean)
const failed = jobs.filter((j, i) => !done[i]).map(j => j.name)
log(`wrote + verified ${ok.length}/${jobs.length}${failed.length ? '; failed: ' + failed.join(', ') : ''}`)

phase('Trends')
const digest = ok.map(r => `- ${r.job.kind} ${r.job.name} (${r.path}, ${r.section}): ${r.headline}`).join('\n')
const trendsTask = mode === 'creators'
  ? `Add (or replace) a section "## What the creator channels are saying (${CREATORS})" placed right after the first ` +
    `paragraph under the title. Sub-sections: "### 10 practical shifts" (each cites guides by path + \`video_id\`s), ` +
    `"### Where creators and conference talks disagree", "### Watch first" (8 creator videos, \`video_id\` — why).`
  : `Maintain a section "## Latest updates" placed right after the first paragraph under the title (create it if missing). ` +
    `Add a sub-section "### ${today}" at its top: 5-10 bullets on what this batch of new videos changes, each citing ` +
    `\`video_id\`s and the guide path. Keep only the 4 newest dated sub-sections; delete older ones.`
const trends = await agent(
  `Update ${ROOT}/kb/trends.md, the "what changed + what to do now" overview for an engineer who builds agent infra.\n` +
  `Docs just written (headlines):\n${digest}\n\nOpen the docs you need (paths above), ${ROOT}/kb/latest.md and ` +
  `${ROOT}/context/profile.md. ${trendsTask}\nDo not change other sections. ${RULES}`,
  { label: 'trends', phase: 'Trends', model: 'haiku', schema: OUT })
return { mode, docs: ok.map(r => ({ path: r.path, section: r.section, verify: r.verify })), failed,
         trends: trends && trends.path }
