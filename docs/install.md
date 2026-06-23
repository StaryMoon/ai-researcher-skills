# Install Notes

The skills are plain directories containing `SKILL.md` files. There is no runtime dependency.

## Codex

```bash
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

Restart the agent session after copying skills if your agent only scans skills at startup.

## Project-local use

You can also keep this repository inside a project and paste the relevant `SKILL.md` into project instructions. This is useful when a team wants a stable shared prompt but does not want to mutate global agent settings.

## Recommended bundle

For an AI researcher workflow, start with:

- `paper-tutorial-briefing`
- `figure-caption-reader`
- `experiment-idea-planner`
- `github-research-maintainer`
