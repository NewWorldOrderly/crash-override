#!/usr/bin/env python3
"""Check that a crash-override theme defines every required colour token.

Usage: python3 scripts/check_theme.py themes/my-theme.css [more.css ...]
Exits 0 if every theme is complete, 1 otherwise. Standard library only.
"""
import re
import sys

REQUIRED = [
    "bg", "surface-1", "surface-2", "surface-3", "border", "border-bright",
    "text-primary", "text-secondary", "text-muted", "accent", "accent-dim",
    "positive", "negative", "warning", "neutral", "grid", "scan",
    "glow-accent", "glow-positive", "glow-negative", "glow-logo", "shadow-overlay",
]

BLOCK = re.compile(r"([^{}@]+)\{([^{}]*)\}")


def check(path):
    text = re.sub(r"/\*.*?\*/", "", open(path).read(), flags=re.S)
    # (theme name, mode) -> set of declared custom properties. Mode is "dark",
    # "light-system" or "light" (the three blocks every theme must have).
    seen = {}
    for sel, body in BLOCK.findall(text):
        m = re.search(r'\[data-theme="([^"]+)"\]', sel)
        if not m:
            continue
        if 'data-mode="light"' in sel:
            mode = "light"
        elif ':not([data-mode="dark"])' in sel:
            mode = "light-system"
        else:
            mode = "dark"
        names = set(re.findall(r"--([a-z0-9-]+)\s*:", body))
        seen.setdefault((m.group(1), mode), set()).update(names)
    if not seen:
        print(f"{path}: no [data-theme=...] blocks found")
        return False
    ok = True
    themes = {t for t, _ in seen}
    for theme in sorted(themes):
        for mode in ("dark", "light-system", "light"):
            names = seen.get((theme, mode))
            if names is None:
                print(f"{path}: theme '{theme}' has no {mode} block")
                ok = False
                continue
            missing = [t for t in REQUIRED if t not in names]
            if missing:
                print(f"{path}: theme '{theme}' ({mode}) is missing: {', '.join(missing)}")
                ok = False
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    results = [check(p) for p in sys.argv[1:]]
    if all(results):
        print("OK: all themes define every required token")
    sys.exit(0 if all(results) else 1)
