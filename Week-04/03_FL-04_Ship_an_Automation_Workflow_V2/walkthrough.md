# FL-04 — Ship an Automation Workflow v2

**Student:** Gungun Sharma  
**Track:** General AI Fluency — Week 4  
**Date:** 25 August 2026

## Workflow selected

**Source-Grounded Weekly Industry Brief**

**Goal:** Turn a small set of trusted source URLs/articles into a concise, source-grounded weekly industry brief with citations, key developments, implications, and a human-review checkpoint.

### Why this workflow?

A weekly industry brief is a repeatable research/writing task where the biggest opportunity is not simply generating text faster. The useful automation is the controlled handoff between evidence gathering, synthesis, drafting, review and formatting. The workflow therefore keeps source grounding at the center and makes human review an explicit final gate.

---

## 1. Step diagram

```text
Trusted sources
      |
      v
[1. GATHER]
Evidence table + source/date tracking
      |
      v
[2. SYNTHESIZE]
3–5 themes + implications + conflicts
      |
      v
[3. DRAFT]
600–800 word industry brief
      |
      v
[4. REVIEW]
Claim-by-claim evidence audit
      |
      v
[5. FORMAT]
Publication-ready brief + checklist
      |
      v
[HUMAN APPROVAL]
Publish / revise / reject
```

**Handoff rule:** each stage receives the previous stage's output; later stages are instructed not to introduce new facts.

---

## 2. Tool stack and configuration

| Stage | Tool | Purpose |
|---|---|---|
| Gather | NotebookLM | Source-grounded extraction and evidence table |
| Synthesize | NotebookLM | Theme grouping while staying inside supplied evidence |
| Draft | Claude Project / structured prompt | Turn approved synthesis into a concise brief |
| Review | Claude Project / review prompt | Audit every important claim against evidence |
| Format | Claude Project / formatting prompt | Produce the final readable version without adding facts |

**Backend/code:** None. This is intentionally a no-code workflow.

**Source rule:** use a small, deliberate set of trusted sources. The workflow is designed around source-grounded material rather than open-ended web generation.

---

## 3. Every prompt/configuration used

### Step 1 — Gather — NotebookLM

**Input:** 5–8 trusted source documents/URLs about one weekly industry topic.

**Prompt:**
```text
You are the research-gathering stage. Use ONLY the sources provided in this notebook.
Extract the facts that are directly supported by the sources. For each useful fact, record:
(1) claim/finding, (2) source, (3) exact supporting passage or location if available,
(4) publication date if available, and (5) why the fact matters.
Do not add outside facts. Flag conflicting claims instead of resolving them by guessing.
Output a structured evidence table.
```

**Handoff:** Evidence table + source list + conflict flags.

### Step 2 — Synthesize — NotebookLM

**Input:** Step 1 evidence table.

**Prompt:**
```text
Using ONLY the evidence gathered in Step 1, group the findings into 3–5 themes.
For each theme provide: theme title, 2–4 supported findings, source references, and a one-sentence
implication. Separate direct evidence from interpretation. If evidence is weak or conflicting,
label it clearly. Do not invent statistics, dates, quotes, companies, or conclusions.
```

**Handoff:** 3–5 themes + supported findings + implications + unresolved questions.

### Step 3 — Draft — Claude Project / structured prompt

**Input:** Synthesized themes and evidence.

**Prompt:**
```text
Draft a 600–800 word weekly industry brief from the supplied synthesis.
Structure:
1. Title
2. Executive summary (3 bullets)
3. What changed this week
4. Why it matters
5. Evidence-backed implications
6. What to watch next
7. Sources
Every factual claim must map to a supplied source. Do not introduce new facts.
Use concise professional language and clearly distinguish evidence from interpretation.
```

**Handoff:** Readable draft with inline source markers and source list.

### Step 4 — Review — Claude Project / review prompt

**Input:** Draft + original evidence table.

**Prompt:**
```text
Audit the draft against the original evidence.
Create a review table with columns: claim, supported source, support status
(SUPPORTED / PARTIAL / UNSUPPORTED), issue, recommended correction.
Check for hallucinated facts, unsupported numbers, missing citations, overclaiming,
source-date errors, contradictions, and wording that turns interpretation into fact.
Do not rewrite silently; report every issue first.
```

**Handoff:** Claim audit + corrections required.

### Step 5 — Format — Claude Project / formatting prompt

**Input:** Reviewed draft + approved corrections.

**Prompt:**
```text
Produce the final publication-ready brief using only the corrected draft.
Keep the approved facts and citations. Use clear headings, short paragraphs, bullets where useful,
and a compact Sources section. Do not add new information during formatting.
At the end include a short 'Human review checklist' with: source accuracy, citation accuracy,
interpretation vs fact, and final tone check.
```

**Handoff:** Final brief + human-review checklist.

## 4. Five real test runs

### Run 1 — Generative AI in software development
- **Inputs:** 5 source documents: official product/company announcements + two reputable technical/news sources
- **Outcome:** Workflow completed end-to-end. Gathered evidence, grouped it into themes, produced a brief, then audited factual claims.
- **Human check:** Verified that product announcements were not treated as independent evidence and checked dates.

### Run 2 — AI regulation and governance
- **Inputs:** 5 source documents: government/regulator pages + reputable policy/technology reporting
- **Outcome:** Workflow completed. Conflicting or differently dated claims were flagged rather than silently merged.
- **Human check:** Checked legal/policy wording and confirmed that the final brief did not present proposals as enacted rules.

### Run 3 — Cloud and AI infrastructure
- **Inputs:** 6 source documents: cloud provider announcements + technical reporting
- **Outcome:** Workflow completed. The synthesis separated announcements from broader industry implications.
- **Human check:** Checked numbers and ensured vendor claims were attributed to the vendor.

### Run 4 — Cybersecurity and generative AI
- **Inputs:** 5 source documents: security advisories/research + reputable reporting
- **Outcome:** Workflow completed. Evidence was grouped by threat, mitigation and operational impact.
- **Human check:** Checked security claims carefully and removed any statement not directly supported by the sources.

### Run 5 — AI hiring and workplace skills
- **Inputs:** 5 source documents: research reports + company/lab publications + reputable reporting
- **Outcome:** Workflow completed. The draft distinguished survey/research findings from interpretation.
- **Human check:** Checked sample/population wording and avoided turning correlation into causation.

## 5. Time accounting

| Activity | Time | Notes |
|---|---:|---|

| **One manual brief** | 45–60 min | Reading, notes, synthesis, drafting and review done sequentially. |
| **Workflow setup** | 35 min | NotebookLM setup, source organization, prompts, output format and review checklist. |
| **Workflow run after setup** | 15–20 min active time | Load sources, run stages, inspect handoffs and perform human checks. |
| **Five-run active time** | ≈ 95 min | Five runs × ~18 min average active handling. |
| **Equivalent manual time for five briefs** | ≈ 225–300 min | Five × 45–60 min. |
| **Estimated active time saved** | ≈ 130–205 min | Excludes initial setup; depends on source quality and review depth. |

The savings estimate is deliberately conservative. It counts active handling time rather than pretending that AI work is instant. Setup time is listed separately because it is a real cost of building the workflow.

---

## 6. Failure points and required human review

### Weak or irrelevant sources
- **What can break:** The workflow may produce a polished but low-value brief.
- **Control:** Use a source-quality gate before Step 1; prefer primary/official sources and reputable reporting.

### Conflicting sources
- **What can break:** Synthesis may accidentally merge incompatible claims.
- **Control:** Step 1 flags conflicts; Step 4 requires explicit conflict checking.

### Citation drift
- **What can break:** A citation may be attached to a nearby claim but not actually support it.
- **Control:** Step 4 audits each material claim against the original evidence table.

### Hallucinated details
- **What can break:** A model may add a plausible fact while drafting.
- **Control:** Drafting prompt forbids new facts; review prompt marks unsupported claims.

### Source date confusion
- **What can break:** Old information can be presented as a new development.
- **Control:** Capture publication date in Step 1 and verify dates during review.

### Over-compression
- **What can break:** Important nuance may disappear in a short brief.
- **Control:** Keep an 'unresolved questions' field and allow human expansion before publication.

### Automation illusion
- **What can break:** The workflow may feel trustworthy because it is repeatable.
- **Control:** Human approval remains mandatory before publication.

## 7. Human review checklist

Before publishing any brief, I must:

- [ ] Confirm every important factual claim is supported by the original source.
- [ ] Check publication dates and whether the source is current enough for the topic.
- [ ] Check that numbers, names, quotes and policy/legal wording are accurate.
- [ ] Separate evidence from interpretation; remove unsupported causal language.
- [ ] Check that competing or conflicting sources are represented fairly.
- [ ] Approve final tone, length and relevance for the intended audience.

## 8. End-to-end acceptance test

**Expected flow:** Sources → Gather/Evidence Table → Synthesize/Themes → Draft/Brief → Review/Claim Audit → Format/Final Brief → Human Approval

A run is considered successful only when:
1. A brand-new topic/input can enter the workflow.
2. The workflow completes all five distinct stages.
3. Each stage produces a visible handoff.
4. The final brief contains only evidence that survived review.
5. Human approval is completed before publication.

---

## 9. What I learned

The main lesson is that automation is not just "one big prompt." The reliability comes from designing explicit stages and handoffs. The Gather stage creates an evidence boundary, Synthesize reduces the evidence into themes, Draft converts those themes into readable writing, Review attacks the draft for unsupported claims, and Format improves presentation without adding facts. This makes the workflow repeatable while keeping the human responsible for final judgment.

## 10. Final result

This workflow is deliberately no-code, free-first and reusable. It can be adapted to a weekly industry brief, source-grounded study notes, or a draft/critique/revise process simply by changing the source set and topic while keeping the same five-stage control structure.

**Final decision:** use the workflow as a repeatable research-to-publication pipeline, with human approval as the final gate.
