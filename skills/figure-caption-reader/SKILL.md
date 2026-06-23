# Figure Caption Reader

## Purpose

Convert paper figures, screenshots, plots, and captions into technical understanding. The output should explain what the visual evidence is trying to prove and what a reader should verify.

## When To Use

Use this skill when the task includes a paper figure, chart, table screenshot, qualitative comparison, pipeline diagram, attention map, architecture figure, or result visualization.

## Inputs

- Image, screenshot, rendered PDF page, or figure crop.
- Caption or surrounding paper text if available.
- Optional paper title and task.
- Optional local experiment logs or baseline numbers.

## Workflow

1. Identify the visual type: architecture, qualitative result, quantitative plot, ablation table, failure case, dataset example, or workflow diagram.
2. Describe only what is visible first. Avoid inventing labels or values that are not legible.
3. Extract the intended claim: what the authors want the figure to prove.
4. Link visual elements to technical concepts: modules, loss terms, data paths, prompts, memory, policy, or benchmark splits.
5. For plots and tables, state the axes, trends, outliers, and comparison groups.
6. For qualitative figures, separate visual impression from measurable evidence.
7. End with a verification checklist: what code, metric, or extra table would confirm the figure's claim.

## Output

- `Visible Content`
- `Intended Claim`
- `Technical Reading`
- `Evidence Strength`
- `Verification Checklist`

## Quality Gates

- Never hallucinate unreadable numbers.
- If text is too small, say so and request a higher-resolution crop or PDF page.
- Distinguish visual quality from metric superiority.
- Do not treat a single cherry-picked qualitative image as proof of general performance.
