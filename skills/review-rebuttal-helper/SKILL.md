# Review Rebuttal Helper

## Purpose

Convert reviewer comments into a clear response plan and concise rebuttal text. The skill is designed for papers, camera-ready changes, artifact reviews, and code-release feedback.

## When To Use

Use this skill when the user provides reviews, editor queries, issue comments, PR feedback, or reviewer objections and wants a response.

## Inputs

- Reviewer comments or GitHub feedback.
- Paper section, experiment log, or code diff if available.
- Constraints such as word limit, tone, venue, or deadline.

## Workflow

1. Split comments into atomic claims or requests.
2. Classify each item: misunderstanding, missing experiment, writing issue, valid limitation, citation request, formatting request, or factual error.
3. For each item, identify available evidence and missing evidence.
4. Draft a response strategy: concede, clarify, add experiment, add citation, or correct.
5. Write concise response text that is polite but specific.
6. Add a camera-ready action list or code action list.
7. If evidence is missing, do not bluff. Mark the answer as pending and propose the quickest evidence collection step.

## Output

- `Reviewer Map`
- `Response Strategy`
- `Draft Rebuttal`
- `Revision Checklist`
- `Evidence Still Needed`

## Quality Gates

- Do not attack the reviewer.
- Do not promise experiments that cannot be run.
- Keep factual corrections grounded in paper text or local evidence.
- Make every promised change traceable to a section, table, figure, or file.
