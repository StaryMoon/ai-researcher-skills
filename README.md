# AI Researcher Skills

> A practical skill pack for AI research agents: paper briefing, figure reading, experiment planning, rebuttal drafting, radar maintenance, and GitHub research upkeep.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-6-blue)](#included-skills)
[![Agent ready](https://img.shields.io/badge/agent-ready-purple)](#install)

AI research work is no longer just reading papers. A useful research agent has to move between PDFs, notes, figures, experiments, GitHub projects, reviews, and daily briefing files without losing context. This repository packages that workflow into small, reusable skills that can be copied into Codex, Claude Code, Cursor, Gemini CLI, or any agent that supports file-backed instructions.

If this saves you time while reading or organizing papers, a star helps other researchers discover it.

## What Makes This Different

- **Research-first skills**: the instructions are written for paper reading, experiment planning, rebuttals, and repo maintenance, not generic office writing.
- **Evidence discipline**: every skill asks the agent to separate paper claims, local evidence, and speculation.
- **Toolchain friendly**: the pack works with Markdown vaults, GitHub repositories, local PDFs, and daily research briefings.
- **Small enough to audit**: each skill is a plain `SKILL.md`, so you can inspect and edit it before giving it to an agent.

## Install

### Codex

Copy one skill folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/paper-tutorial-briefing ~/.codex/skills/
```

Or copy the whole pack:

```bash
cp -R skills/* ~/.codex/skills/
```

### Claude Code / Cursor / Gemini CLI

These tools do not share one universal skill standard, but the content is plain Markdown. Copy the desired `SKILL.md` into your project instructions, rule files, or agent memory folder.

Recommended starting point:

```text
skills/paper-tutorial-briefing/SKILL.md
skills/experiment-idea-planner/SKILL.md
skills/github-research-maintainer/SKILL.md
```

## Included Skills

| Skill | Use it when | Output |
|---|---|---|
| [`paper-tutorial-briefing`](skills/paper-tutorial-briefing/SKILL.md) | You want a paper explained like a serious tutorial, not a shallow abstract summary. | Research briefing with contributions, mechanism, evidence, limitations, and follow-up tasks. |
| [`figure-caption-reader`](skills/figure-caption-reader/SKILL.md) | A paper figure or screenshot needs to be converted into technical understanding. | Figure-by-figure reading notes and evidence map. |
| [`experiment-idea-planner`](skills/experiment-idea-planner/SKILL.md) | You need plausible experiments from a paper idea or existing codebase. | Ranked experiment plan with gates, metrics, risks, and stop rules. |
| [`research-radar-update`](skills/research-radar-update/SKILL.md) | You maintain an awesome list, paper radar, or code-status tracker. | Deduplicated update proposal with paper metadata and status language. |
| [`review-rebuttal-helper`](skills/review-rebuttal-helper/SKILL.md) | You are handling reviewer comments or camera-ready changes. | Claim-by-claim rebuttal map and concise response draft. |
| [`github-research-maintainer`](skills/github-research-maintainer/SKILL.md) | You want a research repo to look credible and easy to review. | README/release/issue/PR checklist with concrete edits. |

## Example Commands

The `commands/` folder contains prompt recipes that compose the skills:

- [`daily-research-brief.md`](commands/daily-research-brief.md): turn papers and repo changes into a daily briefing.
- [`paper-to-experiment.md`](commands/paper-to-experiment.md): convert one paper into a short experiment queue.
- [`repo-release-review.md`](commands/repo-release-review.md): audit whether a research repo is ready to publish.

## Output Style

The skills prefer:

- direct conclusions before long background;
- concrete file paths, paper sections, metric names, and commands;
- explicit uncertainty labels such as `paper claim`, `local evidence`, and `inference`;
- short action lists that a researcher can execute the same day.

## Repository Layout

```text
skills/
  paper-tutorial-briefing/
  figure-caption-reader/
  experiment-idea-planner/
  research-radar-update/
  review-rebuttal-helper/
  github-research-maintainer/
commands/
examples/
docs/
scripts/
release_notes/
```

## Quality Gate

Before publishing an output produced with these skills, check:

- Are all factual claims tied to a paper, file, command output, or cited source?
- Did the agent distinguish reproduced results from paper-reported results?
- Are paths and commands executable in the current workspace?
- Did the output avoid pretending a repo is official when it is only an unofficial starter?

## Related Projects

- [awesome-ai-paper-reproduction-radar](https://github.com/StaryMoon/awesome-ai-paper-reproduction-radar)
- [awesome-llm-reasoning-roadmap](https://github.com/StaryMoon/awesome-llm-reasoning-roadmap)
- [paper-memory-mcp-lite](https://github.com/StaryMoon/paper-memory-mcp-lite)
- [codegraph-memory-mcp-lite](https://github.com/StaryMoon/codegraph-memory-mcp-lite)
- [obsidian-research-brief-kit](https://github.com/StaryMoon/obsidian-research-brief-kit)

## License

MIT.
