# `hands-mlp/` as a git subtree

Upstream:

- `https://github.com/ageron/handson-mlp`
- branch: `main`
- local prefix: `hands-mlp/`

## Add it once

From the root of this repository:

```bash
git remote add handson-mlp https://github.com/ageron/handson-mlp.git
git fetch handson-mlp
git subtree add --prefix=hands-mlp handson-mlp main --squash
```

PowerShell can use the same commands.

The `--squash` option keeps this course repository's history compact while retaining an explicit subtree relationship.

## Update it later

```bash
git fetch handson-mlp
git subtree pull --prefix=hands-mlp handson-mlp main --squash
```

## Verify

```bash
git remote -v
git log --oneline -- hands-mlp
```

Do not manually copy files into `hands-mlp/`; use the subtree commands so future upstream updates remain straightforward.
