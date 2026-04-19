# lsimons-template

Project template for Python CLI tools with standardized tooling.

## Using This Template

1. Click **Use this template** on GitHub (or clone this repo).
2. Clone your new repo locally and run:

   ```bash
   mise install          # pin + install python + uv
   mise run init         # rename `template` → your project name
   mise run install      # install project deps
   ```

   `mise run init` auto-detects your project name from the git remote
   (or directory name), stripping `lsimons-` / `-mono` / `-py` suffixes.
   Pass `--name foo` to override. See `scripts/init.py` for details.

3. Update `AGENTS.md` (and `CLAUDE.md` symlink) with project-specific
   instructions.
4. Replace the placeholder code in `src/<project>/__init__.py` and
   `tests/test_placeholder.py` with your real implementation.

## Included Configuration

- **Python 3.14+** required
- **ruff** for linting and formatting (line-length: 100)
- **basedpyright** strict mode for type checking
- **pytest** with 80% coverage requirement
- **GitHub Actions CI** on push/PR to main, with actions pinned to
  full-length commit SHAs (the repo setting *Require actions to be
  pinned to a full-length commit SHA* is enabled)
- **`.mise.toml`** pins toolchain + defines every repo task

## Project Structure

```
lsimons-template/
├── .github/workflows/ci.yml  # CI pipeline (mise-action)
├── .mise.toml                # Toolchain pin + task runner
├── docs/spec/                # Feature specifications
├── scripts/init.py           # Rename-to-your-project helper
├── src/template/             # Placeholder package (renamed on init)
│   └── __init__.py
├── tests/                    # Test files
├── AGENTS.md                 # AI agent instructions
├── CLAUDE.md -> AGENTS.md    # Claude Code compatibility
├── pyproject.toml            # Project configuration
└── README.md
```

## Development Commands

```bash
mise install          # one-time: pin + install toolchain
mise run install      # install project deps
mise run test         # pytest
mise run lint         # ruff check + format --check
mise run typecheck    # basedpyright
mise run format       # ruff format + --fix
mise run ci           # full CI gate
```

## License

See [LICENSE.md](./LICENSE.md).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
