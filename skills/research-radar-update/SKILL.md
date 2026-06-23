# Research Radar Update

## Purpose

Maintain a paper radar, awesome list, or code-status tracker without turning it into a noisy link dump. The update should add useful metadata and avoid duplicates.

## When To Use

Use this skill when the user wants to update an awesome list, paper reproduction radar, daily paper briefing, or GitHub project catalog.

## Inputs

- Existing README, JSON, CSV, or Markdown table.
- New paper, repo, arXiv link, project page, or GitHub URL.
- Optional category taxonomy.
- Optional code availability status.

## Workflow

1. Inspect the existing schema and category style.
2. Search the current file for duplicate title, abbreviation, arXiv ID, and GitHub repo.
3. Normalize metadata: title, source, area, tags, official code status, implementation status, and why readers search it.
4. Choose the smallest natural insertion point.
5. Use cautious status language. If official code is not indexed locally, do not claim official code does not exist globally.
6. Update badges, counts, or daily notes only if the repository already uses them.
7. Provide a short changelog entry.

## Output

- `Deduplication Check`
- `New Entry`
- `Insertion Point`
- `Status Language`
- `Changelog Note`

## Quality Gates

- Do not add self-links to unrelated lists.
- Do not overstate unofficial repositories as official reproductions.
- Confirm that table pipes, Markdown links, and JSON syntax remain valid.
- Keep the radar useful to readers, not just useful to the maintainer.
