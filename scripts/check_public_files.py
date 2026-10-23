#!/usr/bin/env python3
"""Reject local-only paths in Git's index. This does not scan file contents."""
import subprocess
import sys
from pathlib import PurePosixPath

ROOT_FILES = {"README.md", "LICENSE", "CONTRIBUTING.md", "AGENTS.md", ".gitignore"}
PUBLIC_DIRS = {"research", "products", "templates", "scripts", ".github", ".githooks"}
LOCAL_DIRS = {"private", "work", "outputs", "scratch", "drafts", "discussions", "inbox",
              "__pycache__", ".ipynb_checkpoints", ".venv", "node_modules"}


def allowed(name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        return False
    if not (name in ROOT_FILES or (len(path.parts) > 1 and path.parts[0] in PUBLIC_DIRS)):
        return False
    if any(part in LOCAL_DIRS for part in path.parts):
        return False
    base = path.name.lower()
    return not (base == ".env" or base.startswith(".env.")
                or base.endswith((".pem", ".key", ".pyc"))
                or base in {"credentials.json", "secrets.json", ".ds_store"})


def main():
    paths = subprocess.check_output(["git", "ls-files", "-z"]).decode("utf-8").split("\0")
    if any(name and not allowed(name) for name in paths):
        print("Blocked: local-only or unapproved file paths in Git's index. Review locally with git ls-files.", file=sys.stderr)
        return 1
    print("Public file path check passed. Review file contents before publishing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
