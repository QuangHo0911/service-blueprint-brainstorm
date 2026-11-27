#!/usr/bin/env python3
"""Render a portable, Light-Theme-only standalone HTML Service Blueprint from JSON.

Usage:
    python3 render_blueprint.py <input_data.json> <output.html>
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REQUIRED_TOP_KEYS = [
    "title",
    "businessModel",
    "location",
    "actors",
    "stages",
    "inventoryCatalog",
    "failPoints",
]

REQUIRED_STAGE_KEYS = [
    "id",
    "code",
    "name",
    "goal",
    "timeOffPeak",
    "timePeak",
    "physicalEvidence",
    "digitalEvidence",
    "customerFlows",
    "frontstageSteps",
    "backstageSteps",
    "support",
    "inventoryMapping",
]


def validate_data(data: dict) -> list[str]:
    errors = []
    for k in REQUIRED_TOP_KEYS:
        if k not in data:
            errors.append(f"Missing top-level key: '{k}'")

    stages = data.get("stages", [])
    if not isinstance(stages, list) or not stages:
        errors.append("'stages' must be a non-empty list")
    else:
        for i, st in enumerate(stages):
            for k in REQUIRED_STAGE_KEYS:
                if k not in st:
                    errors.append(f"Stage[{i}] ({st.get('code', '?')}) missing key: '{k}'")
            for f_idx, fl in enumerate(st.get("customerFlows", [])):
                if not isinstance(fl.get("steps"), list) or not fl["steps"]:
                    errors.append(
                        f"Stage[{i}] customerFlows[{f_idx}] must have a non-empty 'steps' list"
                    )
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 render_blueprint.py <input_data.json> <output.html>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1]).expanduser().resolve()
    output_path = Path(sys.argv[2]).expanduser().resolve()
    template_path = Path(__file__).resolve().parent.parent / "resources" / "blueprint-template.html"

    if not input_path.exists():
        print(f"Error: Input JSON not found: {input_path}", file=sys.stderr)
        return 1
    if not template_path.exists():
        print(f"Error: Template HTML not found: {template_path}", file=sys.stderr)
        return 1

    data = json.loads(input_path.read_text(encoding="utf-8"))
    errors = validate_data(data)
    if errors:
        print("Schema validation failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    template = template_path.read_text(encoding="utf-8")
    # Safely serialize JSON for inline <script> context (prevent </script> breakout)
    safe_json = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")

    pattern = re.compile(
        r"/\* === BLUEPRINT_DATA_START === \*/.*?/\* === BLUEPRINT_DATA_END === \*/",
        re.DOTALL,
    )
    if not pattern.search(template):
        print("Error: Template data markers not found.", file=sys.stderr)
        return 1

    replacement = (
        "/* === BLUEPRINT_DATA_START === */\n"
        f"    const BLUEPRINT_DATA = {safe_json};\n"
        "    /* === BLUEPRINT_DATA_END === */"
    )
    rendered = pattern.sub(lambda _: replacement, template, count=1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    # Optional JS syntax verification if node is available
    m = re.search(r"<script>\s*(.*)\s*</script>", rendered, re.DOTALL)
    if m:
        try:
            proc = subprocess.run(
                ["node", "--check"],
                input=m.group(1),
                text=True,
                capture_output=True,
                check=False,
            )
            if proc.returncode != 0:
                print(f"JS syntax check failed:\n{proc.stderr}", file=sys.stderr)
                return 1
        except FileNotFoundError:
            pass

    print(f"OK: Rendered standalone Light-Theme Service Blueprint -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
