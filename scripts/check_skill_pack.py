from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "Purpose",
    "When To Use",
    "Inputs",
    "Workflow",
    "Output",
    "Quality Gates",
]


def main() -> None:
    missing = []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        for heading in REQUIRED:
            if f"## {heading}" not in text:
                missing.append(f"{skill.relative_to(ROOT)} missing ## {heading}")
    if missing:
        raise SystemExit("\n".join(missing))
    print("skill pack check passed")


if __name__ == "__main__":
    main()
