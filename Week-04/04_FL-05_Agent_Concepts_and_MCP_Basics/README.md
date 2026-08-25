# FlyRank AI Internship — FL-05 Final Submission

**Assignment:** Agent Concepts and MCP Basics  
**Track:** General AI Fluency  
**Intern:** Gungun Sharma  

## Submission contents

- `docs/FL05_EXPLAINER.md` — 600–900 word explainer covering workflow vs agent, MCP, three primitives, FL-04 classification, and a concrete agent upgrade.
- `docs/SETUP_AND_EVIDENCE.md` — beginner-friendly Windows setup and evidence procedure.
- `docs/EVALUATION_CHECKLIST.md` — criterion-by-criterion verification.
- `mcp_server/server.py` — bounded local MCP server exposing three tools, a resource, and a prompt.
- `mcp_server/requirements.txt` and `pyproject.toml` — setup metadata.
- `sample_workspace/` — approved demo files used by the MCP tools.
- `tests/test_server.py` — lightweight source/workspace checks.
- `config/claude_desktop_config.example.json` — configuration example only.
- `evidence/screenshots/` — genuine Claude Desktop screenshots captured during the working setup.
- `evidence/tool3_actual_output.txt` — actual Tool #3 output supplied by the intern; supplementary only.
- `reference/assignment_brief/` — screenshots of the FlyRank FL-05 brief/evaluation criteria.

## Verified practical work

The connected `flyrank-fl05` MCP server was verified in Claude Desktop as **running**. The three required tools were executed successfully:

1. `list_workspace_files` — returned the approved local workspace files.
2. `read_workspace_file` — returned the actual contents of `approved_claims.md`.
3. `get_file_metadata` — returned metadata for `approved_claims.md`: 277 bytes, 6 lines, SHA-256 `f17bbb740a9ee7371d6ff0c76443c6297a191c7a1834c32ef8f21c9d1973f79f`.

## Evidence integrity

No fabricated screenshots are included. The screenshots in `evidence/screenshots/` are genuine captures from the working Claude Desktop session.

### Final evidence action

Before uploading this ZIP to FlyRank, add the genuine Claude Desktop screenshot for Tool #3 as:

`evidence/screenshots/03_file_metadata.png`

The screenshot must visibly show the Claude prompt, the MCP/tool call or tool-use indicator, and the returned metadata. Do not edit the screenshot to simulate a tool call.

Once that file is added, the package is ready for final submission.
