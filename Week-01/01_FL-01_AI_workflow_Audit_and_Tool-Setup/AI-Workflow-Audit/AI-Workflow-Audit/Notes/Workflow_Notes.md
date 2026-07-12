# Workflow Notes — AI Workflow Audit

**Author:** Gungun Sharma
**Purpose:** Working notes behind the AI Workflow Audit Report. These are the raw observations and reasoning I used before formalizing the audit table and report.

---

## 1. Current Workflow — A Typical Week

My week currently splits across four buckets: BCA coursework, the FlyRank internship, self-directed AI/DSA learning, and portfolio/GitHub upkeep. Before this audit, I hadn't actually mapped these out — I was just reacting to whatever was due next. Writing it down was the first useful part of this exercise.

A rough breakdown of where my hours go in a normal week:

- **Coursework (BCA):** assignments, lab file write-ups, occasional viva prep
- **FlyRank internship:** frontend tasks, code reviews, standups, documentation
- **AI Engineering learning:** Anthropic Academy modules, small practice projects, reading
- **DSA practice:** daily problems, revisiting weak topics
- **Portfolio/GitHub:** committing work, writing READMEs, cleaning up repos

None of these are new activities. What was new was asking, task by task: *does this need my judgement, or can AI carry some of the weight here?*

## 2. Time-Consuming Work

The tasks that eat the most time are not the hardest ones — they're the repetitive ones with high setup cost:

- Writing boilerplate code (component scaffolding, config files, repetitive CSS)
- First-draft documentation (README files, code comments, commit messages)
- Formatting and re-formatting notes from lectures or course modules into something reusable
- Debugging syntax-level errors that aren't actually logic problems
- Searching for the "correct" way to phrase something in a report or email

These are exactly the tasks where AI collaboration has helped the most, because the cost of a wrong first draft is low and easy to check.

## 3. Where Human Judgement Has to Stay

A few categories where I decided AI should not be doing the primary thinking, even if it assists:

- **Understanding *why* a piece of code works**, not just getting it to run. If I delegate this entirely, I stop learning, which defeats the point of the internship.
- **Architectural decisions** — how to structure a project, which approach fits the actual requirement. AI can suggest options; I have to pick and justify.
- **DSA problem-solving during practice.** Asking AI for the solution directly would make the practice pointless. I only use AI here *after* attempting a problem, to review my approach.
- **Anything going out under my name to FlyRank** — final review of tone, accuracy, and whether it actually reflects what I did.

## 4. Decision-Making Process for AI Use

After going through Anthropic's AI Fluency course, I started applying a simple filter before delegating anything:

1. **Is the task learning-critical for me right now?** If yes, I do it myself first, then use AI to review.
2. **Is the task well-defined with a clear "done" state?** If yes, it's a good delegation candidate.
3. **Is the risk of an unnoticed error high?** If yes, it needs a human-in-the-loop review step, not full automation.
4. **Is this something I'll do again next week?** If yes, it's worth building a reusable prompt or template for.

This is basically the Delegation and Discernment parts of the 4D framework, just applied concretely instead of abstractly.

## 5. AI Collaboration — What Actually Worked

- Giving Claude a clear task description (not just "write a function") produced dramatically better first drafts. Specificity mattered more than the length of the prompt.
- Asking AI to explain its own output — "why did you structure it this way" — caught two cases where I would have accepted code I didn't fully understand.
- Using AI to review my own writing (reports, notes) instead of writing them from scratch kept my own voice while cleaning up structure.
- Iterating in small steps (one function, one section at a time) produced more reliable output than asking for a large piece all at once.

## 6. Verification Process

I did not treat AI output as finished work in any case. My verification steps varied by task type:

- **Code:** ran it, read the diff line by line, checked edge cases, and compared against what I originally intended to build.
- **Documentation:** checked factual claims against the actual project (did the README describe what the code actually does), and rewrote anything that sounded generic.
- **Analysis/report content:** cross-checked numbers and classifications against my own logged observations, not against what "sounded right."
- **DSA reviews:** re-derived the AI's suggested approach by hand before accepting it as correct.

The one rule I kept consistent: if I couldn't explain *why* something was correct, I hadn't verified it — I had just read it.

## 7. Reflection

Doing this audit made a difference I didn't expect going in. I assumed I'd end up with a report that said "delegate more to AI." Instead, I ended up with a much more specific map: delegate the repetitive, low-risk, well-specified tasks; collaborate on medium-complexity work where I still need to be in the loop; and keep full ownership of anything that's actually building my skill or judgement.

The biggest shift in my actual behavior: I stopped asking AI to "do" a task and started asking it to do a *specific part* of a task, with me handling the parts that required context only I had. That single change improved both the quality of the output and how much I retained from doing the work.

Next step is turning this from a one-time audit into a habit — revisiting the table monthly instead of writing it once and forgetting about it.
