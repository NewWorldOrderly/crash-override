# crash-override

A themeable CSS design system with a hacker-movie look. Plain CSS variables (design tokens) and
themes that work in any framework, or none. No build step, no dependencies.

Built first for a handful of personal projects, but meant for anyone to use on any project.

## Use it

```html
<link rel="stylesheet" href="tokens/core.css">
<link rel="stylesheet" href="themes/zero-cool.css">

<html data-theme="zero-cool">            <!-- follows the system's light/dark setting -->
<html data-theme="zero-cool" data-mode="light">   <!-- or force "light" or "dark" -->
```

Then style with the variables: `background: var(--bg); color: var(--text-primary);`.
Open `preview.html` in a browser to see every theme and mode.

## Built-in themes

Named for the characters of *Hackers* (1995). Every theme has a dark and a light mode. In the red and green themes the status colours are deliberately a different hue from the accent (`--negative` is orange-red in Acid Burn, `--positive` is teal-mint in Cereal Killer), so "chrome" and "good/bad" never share a colour.

| Theme | Look |
|---|---|
| `zero-cool` | Cyan phosphor on near-black. Light mode is a "paper terminal". |
| `gibson` | Amber/orange phosphor on warm black. |
| `acid-burn` | Crimson red on blood-black. Light mode is rose paper. |
| `cereal-killer` | Phosphor green on black. Light mode is green-tinged paper. |

## The token contract

Every theme must define these (the full list is in `scripts/check_theme.py`):

- **Surfaces and lines:** `--bg`, `--surface-1/2/3`, `--border`, `--border-bright`, `--grid`
- **Text:** `--text-primary`, `--text-secondary`, `--text-muted`
- **Accent:** `--accent`, `--accent-dim`
- **Status:** `--positive`, `--negative`, `--warning`, `--neutral`
- **Effects:** `--scan`, `--glow-accent`, `--glow-positive`, `--glow-negative`, `--glow-logo`, `--shadow-overlay`

`tokens/core.css` provides the non-colour tokens (type, spacing, radius, motion). They have
defaults, and a theme may override any of them.

Status colours are generic on purpose: `--positive` is "good" and `--negative` is "bad"
whatever your app is about. Colours specific to your app belong in your app, built on these.

## Make your own theme

1. Copy `themes/_template.css` to `themes/my-theme.css` and replace `my-theme` with your name.
2. Set every variable in all three blocks (dark, light by system setting, light forced).
3. Check it: `python3 scripts/check_theme.py themes/my-theme.css`. It lists any missing token.
4. Use it with `data-theme="my-theme"`.

## Status

Tokens and themes only. Components (buttons, cards, tables, dialogs) will be added as real
screens need them, as plain CSS classes first.

## Licence

MIT.
