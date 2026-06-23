# Experiment Idea Planner

## Purpose

Turn a paper idea, codebase, or research hunch into a ranked experiment plan with concrete gates. The plan should help a researcher avoid wasting GPU time on weak branches.

## When To Use

Use this skill when the user asks what to try next, how to improve a model, how to reproduce a paper, how to compare branches, or how to design a short research sprint.

## Inputs

- Current hypothesis or paper idea.
- Local code path and current baseline.
- Available compute budget.
- Metric, dataset, or validation split.
- Prior failed attempts if available.

## Workflow

1. Restate the target metric and baseline. If they are absent, ask for them or define a minimal proxy.
2. Convert broad ideas into small experiment candidates.
3. Rank candidates by expected value, cost, and interpretability.
4. For each candidate, define implementation scope, config knobs, required files, and expected failure mode.
5. Add a gate: minimal metric improvement, qualitative signal, runtime ceiling, or ablation sanity check.
6. Add a stop rule for weak branches.
7. Produce the first command or file-edit route when the codebase is available.

## Output

- `Baseline`
- `Ranked Experiment Queue`
- `Quick Gates`
- `Stop Rules`
- `First Implementation Step`
- `What Would Be Publishable`

## Quality Gates

- Do not propose expensive full runs before a quick gate.
- Keep comparisons on the same validation slice.
- Avoid adding complexity without a measurable reason.
- If the baseline is unverified, make baseline verification experiment 0.
