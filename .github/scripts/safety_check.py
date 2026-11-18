"""Safety check for the marketing-leads plugin. Runs on every push and pull request.

It keeps SECURITY.md true. The build fails if the plugin gains anything that
could reach outside the conversation or change files:

- a connector (MCP server), hook, agent or command
- a file type other than Markdown, JSON or Python
- a Python import outside the short allowed list (no network, no shell, no OS access)
- a call that writes, deletes, runs code or opens a connection

Run it locally with: python .github/scripts/safety_check.py
"""

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLUGIN = ROOT / "plugins" / "marketing-leads"

ALLOWED_SUFFIXES = {".md", ".json", ".py"}
FORBIDDEN_PATHS = ["hooks", "agents", "commands", ".mcp.json", "mods", "bin"]
FORBIDDEN_MANIFEST_KEYS = {"mcpServers", "hooks", "agents", "commands", "lspServers", "mods"}

# Standard library modules that read data only, plus pandas to read the export.
ALLOWED_IMPORTS = {"argparse", "io", "json", "re", "sys", "zipfile", "pathlib", "pandas"}

# Calls and attributes that write, delete, execute or connect.
FORBIDDEN_CALLS = {
    "eval", "exec", "compile", "__import__", "open", "input", "breakpoint",
}
FORBIDDEN_ATTRS = {
    "to_csv", "to_excel", "to_json", "to_parquet", "to_pickle", "to_sql", "to_html",
    "write", "write_text", "write_bytes", "writestr", "unlink", "rmdir", "mkdir",
    "rename", "replace", "touch", "chmod", "extractall", "extract", "system", "popen",
    "read_html", "read_sql", "read_pickle",
}


def fail(errors):
    print("Safety check FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)


def check_files(errors):
    for p in PLUGIN.rglob("*"):
        rel = p.relative_to(ROOT)
        if any(part in FORBIDDEN_PATHS for part in p.relative_to(PLUGIN).parts):
            errors.append(f"{rel}: plugins here must not contain hooks, agents, commands, connectors or binaries")
        if p.is_file() and p.suffix.lower() not in ALLOWED_SUFFIXES:
            errors.append(f"{rel}: file type {p.suffix or '(none)'} is not allowed (Markdown, JSON or Python only)")


def check_manifest(errors):
    manifest = PLUGIN / ".claude-plugin" / "plugin.json"
    data = json.loads(manifest.read_text())
    for key in FORBIDDEN_MANIFEST_KEYS & set(data):
        errors.append(f"{manifest.relative_to(ROOT)}: key '{key}' is not allowed")


def check_python(errors):
    for py in PLUGIN.rglob("*.py"):
        rel = py.relative_to(ROOT)
        tree = ast.parse(py.read_text(), filename=str(rel))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [(node.module or "").split(".")[0]]
            else:
                names = []
            for n in names:
                if n not in ALLOWED_IMPORTS:
                    errors.append(f"{rel}:{node.lineno}: import '{n}' is not on the allowed list")
            if isinstance(node, ast.Call):
                f = node.func
                if isinstance(f, ast.Name) and f.id in FORBIDDEN_CALLS:
                    errors.append(f"{rel}:{node.lineno}: call '{f.id}()' is not allowed")
                if isinstance(f, ast.Attribute) and f.attr in FORBIDDEN_ATTRS:
                    errors.append(f"{rel}:{node.lineno}: call '.{f.attr}()' is not allowed")


def main():
    errors = []
    check_files(errors)
    check_manifest(errors)
    check_python(errors)
    if errors:
        fail(errors)
    print("Safety check passed: no connectors, hooks, agents or commands; Markdown, JSON and Python only;")
    print("the script imports only " + ", ".join(sorted(ALLOWED_IMPORTS)) + ", and makes no write, delete, run or network calls.")


if __name__ == "__main__":
    main()
