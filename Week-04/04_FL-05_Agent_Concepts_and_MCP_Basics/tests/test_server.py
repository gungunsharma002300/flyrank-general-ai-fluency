from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp_server"))

def test_server_source_contains_three_required_tools():
    source = (ROOT / "mcp_server" / "server.py").read_text(encoding="utf-8")
    assert "def list_workspace_files" in source
    assert "def read_workspace_file" in source
    assert "def get_file_metadata" in source

def test_demo_files_exist():
    workspace = ROOT / "sample_workspace"
    assert (workspace / "project_facts.json").exists()
    assert (workspace / "approved_claims.md").exists()
    assert (workspace / "sample_notes.txt").exists()
