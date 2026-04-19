"""Minimal package so the coverage target resolves.

Replace with your real code. `mise run init` renames this package to
`<your-project>` in all files + this directory.
"""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
