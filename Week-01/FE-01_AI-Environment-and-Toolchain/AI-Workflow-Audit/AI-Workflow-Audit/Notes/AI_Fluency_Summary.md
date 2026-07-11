# AI Fluency Summary — Anthropic Academy

**Author:** Gungun Sharma
**Course:** AI Fluency (Anthropic Academy)
**Purpose:** A working summary of the course, written in my own words, for future reference and to support the AI Workflow Audit.

---

## 1. What "AI Fluency" Actually Means

Before this course, I thought of "using AI well" as basically "writing good prompts." AI Fluency is a broader idea: it's the ability to work *with* generative AI systems in a way that produces reliable, high-quality outcomes while staying accountable for the result. Prompting is one piece of it. Judgement, verification, and communication are the rest.

The course frames fluency as a practical skill, not a technical one — you don't need to understand model architecture to be fluent, you need to understand how to direct, judge, and check the output of a system that is capable but not accountable for being wrong.

## 2. Generative AI — The Basics, Without the Hype

Generative AI systems like Claude produce output by predicting likely continuations based on patterns learned from large amounts of text (and other data). A few practical implications the course kept coming back to:

- The model doesn't "know" things the way a person does — it generates plausible text, which is usually correct but is not guaranteed to be.
- It has no persistent memory of you unless a system is built to provide that context (like a Claude Project).
- It doesn't inherently know your specific situation, codebase, or constraints — it only knows what you tell it, plus whatever it can look up.
- Confidence in tone is not the same as confidence in correctness. A wrong answer and a right answer can sound equally certain.

This last point matters more than it sounds — it's the reason verification is treated as a core skill, not an optional step.

## 3. The 4D Framework

This is the core model the course teaches for working with AI, and the one I used to structure my own workflow audit.

### Delegation
Deciding *what* to hand to AI and *how much* control to give up. Delegation exists on a spectrum:
- **Just Me** — no AI involvement; the task requires human judgement throughout.
- **Collaborate with AI** — back-and-forth, AI assists but I stay in the loop on decisions.
- **Delegate to AI with Review** — AI does the first pass, I review and approve before it's final.
- **Fully Automate** — AI handles the task end-to-end with no per-instance review, appropriate only for low-risk, well-defined, repetitive tasks.

The mistake I was making before the course was treating this as one setting for "AI use" overall, instead of a decision made per task.

### Description
The quality of AI output is largely a function of how well the task is described. A good description gives:
- The actual goal, not just the immediate instruction
- Relevant context (constraints, prior decisions, style/format expectations)
- What "done" looks like
- Examples, when the format matters

Vague descriptions don't just produce worse output — they produce *confidently* worse output, which is harder to catch.

### Discernment
The ability to judge AI output critically instead of accepting it because it's fluent and fast. Discernment means:
- Noticing when an answer is generic rather than specific to your actual situation
- Checking claims against something other than "it sounds right"
- Recognizing when a task was actually more ambiguous than the AI's confident answer suggests
- Knowing your own domain well enough to catch a plausible-but-wrong answer

### Diligence
Following through responsibly on delegated work — not disappearing after prompting. Diligence includes:
- Actually reviewing what was delegated, proportional to the task's risk
- Taking ownership of the final output, since "the AI wrote it" isn't an excuse for an error that ships
- Iterating instead of accepting the first draft when something's off
- Documenting what was AI-assisted, so the process stays transparent

## 4. Prompt Engineering, Reframed

The course treats prompt engineering as an extension of Description, not a separate magic skill. The practices that actually held up:
- Being specific about the desired output format, not just the topic
- Providing constraints up front rather than correcting after the fact
- Breaking large tasks into smaller, checkable steps
- Giving the model relevant context instead of assuming it can infer your situation
- Asking the model to explain its reasoning when the task is non-trivial, which also makes verification easier

## 5. Responsible AI Use

A recurring theme was that "responsible" isn't a separate checklist bolted onto AI use — it's what Delegation, Description, Discernment, and Diligence add up to when done properly. Specific practices from the course:
- Being transparent about what was AI-assisted versus fully human-authored, especially in academic and professional submissions
- Not delegating tasks where the *process* of doing the work is the actual point (like DSA practice, or graded coursework meant to test my own understanding)
- Treating AI as a capable but non-accountable collaborator — the accountability for the final output stays with the human
- Being mindful of overreliance: using AI in a way that keeps my own skills growing, not replacing them

## 6. Verification — Treated as a Core Skill, Not an Afterthought

The course dedicates real attention to verification because Discernment and Diligence both depend on it. Verification approaches that map to my own work:
- **Code:** run it, test edge cases, read the actual diff rather than skimming the summary
- **Factual/analytical content:** check against a source you trust, not against how confident the answer sounds
- **Writing:** check it still reflects your actual voice and actual situation, not a generic version of it

The course's underlying point: verification effort should scale with risk, not be uniform. A low-stakes boilerplate function needs a quick check; something that affects a grade, a deliverable, or a decision needs a real one.

## 7. Best Practices — Condensed

- Match the delegation level to the task's risk and learning value, not to how tedious the task feels.
- Write descriptions that include the goal and the constraints, not just the instruction.
- Review AI output proportional to what's at stake if it's wrong.
- Keep a record of what was AI-assisted — it protects both accuracy and accountability.
- Revisit your own AI-use decisions periodically; the right classification for a task can change as your skills grow.

## 8. Reflection

The most useful shift the course produced in me wasn't a new prompting trick — it was replacing a vague instinct ("should I use AI for this?") with an actual framework I can apply consistently. The Workflow Audit Table in this submission is a direct application of that framework to my real week, not a theoretical exercise.
