#!/usr/bin/env python3
"""Pre-publish checks: tracked paths, file types, product frontmatter, stub bodies, aliases, dates, list links.

Does not scan file contents for sensitive text; still read the diff before publishing.
"""
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
ROOT_FILES = {"README.md", "LICENSE", "AGENTS.md", ".gitignore"}
PUBLIC_DIRS = {"products", "lists", "articles", "templates", "scripts", ".github", ".githooks"}
EXTS = {".md", ".csv", ".py", ".sh", ".yml", ".yaml", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
NO_EXT_OK = {".githooks/pre-commit"}
PRODUCT_KEYS = {"id", "name", "website", "status", "updated"}
STATUSES = {"stub", "draft", "done"}


def tracked():
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8")
    return [p for p in out.split("\0") if p]


def check_path(name):
    path = PurePosixPath(name)
    if name in ROOT_FILES:
        return None
    if len(path.parts) < 2 or path.parts[0] not in PUBLIC_DIRS:
        return "outside public directories"
    if "private" in path.parts:
        return "private path"
    if name not in NO_EXT_OK and path.suffix.lower() not in EXTS:
        return "file type not allowed (raw third-party files stay in private/)"
    if path.name.startswith(".env") or path.suffix in {".pem", ".key"}:
        return "credential-like file"
    return None


def parse_doc(text):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return None, ""
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    body = re.sub(r"<!--.*?-->", "", m.group(2), flags=re.S).strip()
    return meta, body


def parse_list_field(raw):
    return [s.strip().strip("\"'") for s in re.findall(r'"([^"]+)"|\'([^\']+)\'', raw or "") for s in s if s]


def main():
    errors, warnings = [], []
    for name in tracked():
        reason = check_path(name)
        if reason:
            errors.append(f"{name}: {reason}")

    for f in sorted((ROOT / "products").glob("*.md")):
        meta, body = parse_doc(f.read_text(encoding="utf-8"))
        if meta is None:
            errors.append(f"products/{f.name}: missing frontmatter")
            continue
        missing = sorted(k for k in PRODUCT_KEYS if not meta.get(k))
        if missing:
            errors.append(f"products/{f.name}: missing {', '.join(missing)}")
        if meta.get("id") and meta["id"] != f.stem:
            errors.append(f"products/{f.name}: id '{meta['id']}' does not match filename")
        status = meta.get("status")
        if status and status not in STATUSES:
            errors.append(f"products/{f.name}: status must be one of {sorted(STATUSES)}")
        if status == "stub" and len([ln for ln in body.splitlines() if ln.strip()]) > 1:
            errors.append(f"products/{f.name}: stub must have empty or single-line body")
        comp = re.sub(r"\s*[\(（].*?[\)）]", "", meta.get("company", "")).strip().lower()
        for alias in parse_list_field(meta.get("aliases", "")):
            if comp and alias.lower() == comp:
                errors.append(f"products/{f.name}: alias '{alias}' duplicates company '{meta.get('company')}'")
        fl = meta.get("first_launch", "")
        if re.match(r"^\d{4}-\d{2}-01$", fl):
            warnings.append(f"products/{f.name}: first_launch '{fl}' looks like a -MM-01/-01-01 placeholder")

    for f in sorted((ROOT / "lists").glob("*.md")):
        for target in re.findall(r"\]\((\.\./products/[^)#]+\.md)\)", f.read_text(encoding="utf-8")):
            if not (f.parent / target).resolve().exists():
                errors.append(f"lists/{f.name}: missing profile {target}")

    for w in warnings:
        print(f"Warning: {w}", file=sys.stderr)
    if errors:
        print("Check failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("Check passed. Read the diff before publishing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
