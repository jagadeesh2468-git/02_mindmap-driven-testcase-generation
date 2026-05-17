"""
Parse XMind mindmap files and convert them into structured formats
suitable for feeding to Copilot as prompt context.

Usage:
    python mindmap_parser.py <path_to.xmind> [output.json]
"""

import json
import sys
from pathlib import Path

try:
    import xmindparser
except ImportError:
    raise SystemExit("Install xmindparser first: pip install xmindparser")


def parse_mindmap(xmind_path: str) -> list:
    return xmindparser.xmind_to_dict(xmind_path)


def save_as_json(content: list, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    print(f"Saved: {output_path}")


def flatten_nodes(node: dict, depth: int = 0) -> list:
    result = []
    title = node.get("title", "").strip()
    if title:
        result.append({"depth": depth, "title": title})
    for child in node.get("topics", []):
        result.extend(flatten_nodes(child, depth + 1))
    return result


def to_prompt_context(xmind_path: str) -> str:
    """
    Convert an XMind file to plain text usable as Copilot prompt context.

    Output format:
        Module: <sheet title>
          - <root node>
            - <child node>
              - <grandchild node>
    """
    content = parse_mindmap(xmind_path)
    lines = []
    for sheet in content:
        lines.append(f"Module: {sheet.get('title', 'Untitled')}\n")
        root = sheet.get("topic", {})
        for node in flatten_nodes(root):
            indent = "  " * node["depth"]
            lines.append(f"{indent}- {node['title']}")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mindmap_parser.py <file.xmind> [output.json]")
        sys.exit(1)

    xmind_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output/parsed_mindmap.json"

    content = parse_mindmap(xmind_path)
    save_as_json(content, output_path)

    print("\n--- Prompt context preview ---\n")
    print(to_prompt_context(xmind_path))
