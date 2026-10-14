# AI Prompting Framework for HR Professionals

A practical guide to getting consistently useful results from AI assistants for HR work — from job descriptions and policies to interview design and employee communications.

---

## Why HR Needs Its Own Framework

Generic prompting advice ("be specific") doesn't account for what makes HR work distinct: the legal exposure, the confidentiality of employee data, the sensitivity of tone, and the fact that most HR outputs speak on behalf of the organization, not an individual. A good HR prompt therefore carries more context than most — the audience, the company voice, the compliance boundaries, and the stakes of getting it wrong.

This guide is built around the **SCOPE** framework, five elements that should appear in nearly every HR prompt.

---

## The SCOPE Framework

**S — Situation.** Give the AI the business context a new HR colleague would need. What's happening, why, and what has already been decided.

**C — Constraints.** Legal, policy, and practical boundaries. Jurisdiction, applicable laws, company policies, word limits, what must be included, and what must never appear.

**O — Output.** The exact deliverable: format, length, structure, and how it will be used. "A one-page FAQ for the intranet" produces a very different result than "an email from the CHRO."

**P — Persona & audience.** Whose voice is this in, and who reads it? A message to hourly warehouse staff should not read like one to the executive team.

**E — Examples & exclusions.** Show what good looks like (paste a past document you liked) and name what to avoid (jargon, legalese, over-promising, specific phrases your legal team has flagged).

### SCOPE in Action

Weak prompt:

```
Write a job description for a marketing manager.
```

SCOPE prompt:

```
Situation: We're a 200-person B2B software company hiring our first
Marketing Manager to build a team of 3 over the next year. The role
reports to the VP of Sales.

Constraints: US-based, remote-eligible. Include a salary range of
$95k–$120k (required by state pay transparency law). No degree
requirement — skills-based only. Avoid gendered or age-coded language.

Output: A job description under 500 words with sections for About Us,
The Role, What You'll Do, What You Bring, and Benefits.

Persona & audience: Warm but professional company voice. Audience is
mid-career marketers who are likely employed and passively looking.

Examples & exclusions: Avoid clichés like "rockstar," "fast-paced,"
"wear many hats," and "work hard play hard." Here's a JD we liked
last year for tone: [paste example]
```

The second prompt takes two minutes longer to write and saves five rounds of revision.

---

## The HR Guardrails Layer

Before applying SCOPE, run every task through three questions.

**1. Is there personal data in this prompt?** Never paste employee names, IDs, health information, salary details tied to individuals, or investigation specifics into a tool unless your organization has approved it for that data. Anonymize first: "Employee A, a 4-year tenured analyst" works as well as a real name.

**2. Is this a judgment call or a drafting task?** AI is excellent at drafting, summarizing, structuring, and generating options. It should not decide who gets hired, promoted, disciplined, or terminated. Many jurisdictions (and emerging AI regulations like the EU AI Act and NYC Local Law 144) treat automated employment decisions as high-risk. Use AI to prepare the materials for human decisions, not to make them.

**3. Does the output need expert review?** Anything touching legal compliance, accommodations, terminations, investigations, or benefits should be treated as a first draft for counsel or a senior reviewer — and your prompt should say so: "This is a draft for legal review; flag any statements that could create contractual obligations."

---

## Use-Case Playbook

### Recruiting & Job Descriptions

Ask for skills-based language, an inclusive-language check, and a readability pass. Useful follow-up prompt after any JD draft:

```
Review this job description for language that could discourage
qualified candidates — gendered terms, age-coded phrases,
unnecessary requirements, or corporate jargon. List each issue,
explain why it's a problem, and suggest a replacement.
```

### Interview Design

Have the AI generate structured, job-related questions with scoring anchors, which improves consistency and defensibility:

```
Create 6 behavioral interview questions for a Customer Support Lead
role, each targeting one of these competencies: de-escalation,
coaching, prioritization. For each question, provide a 1–5 scoring
rubric describing what a weak, acceptable, and strong answer looks
like. All questions must be job-related and legally safe to ask in
the US.
```

### Policy Drafting & Updates

Give the AI your existing policy plus the change, and ask for a redline-style summary:

```
Here is our current PTO policy: [paste]. We're moving from accrual
to a flexible PTO model effective Jan 1. Draft the updated policy,
then list every substantive change from the old version in a table
so I can walk our leadership team through it.
```

### Employee Communications

Specify the emotional register explicitly — this is where AI drafts most often miss:

```
Draft an all-hands email announcing that our office is relocating
15 miles north in March. Tone: acknowledge this is genuinely
inconvenient for some commutes, don't oversell it as exciting.
Include what's decided, what's still open, and where to send
questions. Under 250 words. From the COO.
```

### Performance & Feedback

Use AI to convert manager notes into specific, behavioral feedback — never to invent content:

```
Here are my rough notes from observing this quarter: [paste notes].
Turn these into 3 pieces of feedback using the SBI format
(Situation–Behavior–Impact). Only use what's in my notes — do not
add examples I didn't provide. Flag any note that's too vague to
be actionable so I can gather more detail.
```

### HR Analytics & Reporting

AI can structure analysis and draft narratives, but verify every number:

```
Here is our anonymized quarterly attrition data by department:
[paste]. Identify the three most significant patterns, draft a
one-paragraph executive summary for each, and list what additional
data would help explain the trend. Do not speculate about causes
the data doesn't support.
```

---

## Iteration Techniques That Work

**Ask for options, not answers.** "Give me three versions: one formal, one warm, one brief" is faster than revising one draft three times.

**Make the AI interview you.** For complex tasks: "Before drafting, ask me the 5 most important questions you need answered to do this well." This surfaces context you didn't think to include.

**Use the critique loop.** After any draft: "Now critique this from the perspective of a skeptical employee / an employment lawyer / a candidate we rejected." This catches problems before they ship.

**Anchor with your best work.** Pasting one strong past example teaches tone faster than a paragraph of adjectives ever will.

**Name the failure mode.** If drafts keep coming back too long, too stiff, or too salesy, say so directly: "Your last version was too corporate — write like a trusted colleague, not a press release."

---

## Quick Reference Card

Before sending any HR prompt, check:

**S** — Did I explain the situation and context?
**C** — Did I state legal, policy, and format constraints?
**O** — Did I define the exact output and its use?
**P** — Did I set the voice and name the audience?
**E** — Did I give an example and list exclusions?

And the guardrails: no identifiable personal data, no delegated employment decisions, expert review for anything with legal weight.

---

*Treat every AI output as a strong first draft from a capable new team member: usually 80% there, always worth a careful read, and never sent without a human's name behind it.*
