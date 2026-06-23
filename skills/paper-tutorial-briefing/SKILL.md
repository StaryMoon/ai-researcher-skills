# Paper Tutorial Briefing

## Purpose

Turn an AI paper into a rigorous but readable tutorial briefing. The goal is not to paraphrase the abstract; the goal is to help a researcher understand what the paper changes, what evidence supports it, and what should be tried locally next.

## When To Use

Use this skill when the user gives a paper PDF, arXiv link, title, project page, README, or local paper note and asks for a technical explanation, tutorial, daily briefing entry, or research direction.

## Inputs

- Paper PDF, URL, title, or extracted text.
- Optional code repository or project page.
- Optional local research context, baseline, metric, or dataset.
- Optional target audience such as beginner, reviewer, implementer, or project maintainer.

## Workflow

1. Identify the paper metadata: title, venue or preprint status, authors if available, task, model family, and main artifact.
2. Produce a one-sentence takeaway that states the technical move, not the marketing claim.
3. Extract the contribution stack: problem setting, key mechanism, training or inference recipe, evidence, and stated limitations.
4. Build an evidence map. Separate paper-reported metrics, qualitative figures, ablations, and any local evidence.
5. Explain the method with one concrete implementation mental model: tensors, modules, prompts, losses, memory, data flow, or evaluation loop.
6. Identify reproduction risk: missing details, compute assumptions, hidden preprocessing, dataset ambiguity, or metric mismatch.
7. End with next actions: shortest faithful experiment, stop rule, and what result would justify adding it to a repo or briefing.

## Output

Use this structure unless the user asks otherwise:

- `One-Sentence Takeaway`
- `Why This Paper Exists`
- `Core Mechanism`
- `Evidence Map`
- `Implementation Notes`
- `Reproduction Risks`
- `Next Local Actions`

## Quality Gates

- Do not claim results were reproduced unless local commands or logs prove it.
- Mark uncertainty explicitly: `paper claim`, `local evidence`, or `inference`.
- Prefer named metrics, datasets, and ablations over vague praise.
- If the paper text is unavailable, say what is missing and base the briefing only on accessible sources.
