# UV usage

https://github.com/astral-sh/uv

## Installation
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Initialize new project
```bash
uv init curricubook
```

## Add a dependency
```bash
uv add dependency-name
```

## Check project with ruff
```bash
uv add ruff
uv run ruff check
```

## Generate lock file

About lockfiles: https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment

```bash
# Check if up to date
uv lock --check

# Generate lockfile
uv lock
```
