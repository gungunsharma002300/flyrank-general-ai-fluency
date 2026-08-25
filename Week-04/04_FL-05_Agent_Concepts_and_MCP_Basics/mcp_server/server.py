"""FlyRank FL-05 Local Evidence MCP Server.

This server is intentionally bounded to the repository's sample_workspace folder.
It exposes:
- tools: list/read/metadata operations
- a resource: workspace://overview
- a prompt: evidence_review

Run directly for an MCP stdio host:
    python server.py
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from mcp.server import MCPServer

BASE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE = (BASE_DIR / "sample_workspace").resolve()

mcp = MCPServer("FlyRank FL-05 Local Evidence")


def _safe_path(relative_path: str) -> Path:
    """Resolve a path only if it stays inside the demo workspace."""
    candidate = (WORKSPACE / relative_path).resolve()
    if candidate != WORKSPACE and WORKSPACE not in candidate.parents:
        raise ValueError("Access denied: path is outside the demo workspace.")
    if not candidate.exists():
        raise FileNotFoundError(f"File not found: {relative_path}")
    return candidate


@mcp.tool()
def list_workspace_files() -> str:
    """List files available inside the approved local demo workspace."""
    files = sorted(
        p.relative_to(WORKSPACE).as_posix()
        for p in WORKSPACE.rglob("*")
        if p.is_file()
    )
    return "\n".join(files) if files else "(workspace is empty)"


@mcp.tool()
def read_workspace_file(relative_path: str) -> str:
    """Read UTF-8 text from one approved file in the local demo workspace."""
    path = _safe_path(relative_path)
    if path.stat().st_size > 100_000:
        raise ValueError("File is too large for this demonstration.")
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_file_metadata(relative_path: str) -> str:
    """Return size, line count, and SHA-256 for one approved local file."""
    path = _safe_path(relative_path)
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    line_count = len(text.splitlines())
    digest = hashlib.sha256(raw).hexdigest()
    return (
        f"path: {path.relative_to(WORKSPACE).as_posix()}\n"
        f"size_bytes: {len(raw)}\n"
        f"line_count: {line_count}\n"
        f"sha256: {digest}"
    )


@mcp.resource("workspace://overview")
def workspace_overview() -> str:
    """Describe the purpose and safety boundary of the demo workspace."""
    return (
        "FlyRank FL-05 local evidence workspace. "
        "Only files under sample_workspace are exposed by the tools."
    )


@mcp.prompt()
def evidence_review(task: str = "verify a project claim") -> str:
    """Create a reusable prompt for evidence-oriented review."""
    return (
        "Review the following task using only evidence retrieved from the "
        "connected FlyRank FL-05 Local Evidence MCP server. "
        f"Task: {task}. State which tool results support your conclusion."
    )


if __name__ == "__main__":
    mcp.run()
