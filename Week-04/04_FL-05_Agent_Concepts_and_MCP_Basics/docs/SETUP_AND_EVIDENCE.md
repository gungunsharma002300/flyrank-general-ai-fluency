# FL-05 — Setup and Real Evidence Guide

This guide is written for a beginner on Windows.

## 1. Requirements

You need:
- Python 3.10 or newer.
- Claude Desktop installed and signed in.
- This project folder extracted somewhere simple, for example:
  `C:\Users\<YourName>\Desktop\FlyRank_FL-05_Gungun_Sharma_Submission`

No paid API key is required for the included local MCP server.

## 2. Install the MCP Python SDK

Open PowerShell inside the `mcp_server` folder:

```powershell
cd "C:\path\to\FlyRank_FL-05_Gungun_Sharma_Submission\mcp_server"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, you can skip activation and use:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Test the server locally

From `mcp_server`:

```powershell
python server.py
```

The process will wait because MCP/stdio is designed for a host to launch it. Stop it with `Ctrl+C`.

A more useful development check is:

```powershell
python -m pytest
```

If pytest is not installed, run:

```powershell
pip install pytest
python -m pytest
```

## 4. Connect the server to Claude Desktop

The easiest route is to use the MCP SDK's installer if the `mcp` CLI is available:

```powershell
mcp install server.py --name "FlyRank FL-05 Local Evidence"
```

If you use the virtual environment and the command is not found:

```powershell
.\.venv\Scripts\mcp.exe install server.py --name "FlyRank FL-05 Local Evidence"
```

The SDK writes a Claude Desktop entry with an absolute path.

Windows Claude Desktop MCP configuration is stored under:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

If you need to edit it manually, merge the example in `config/claude_desktop_config.example.json` into the existing `mcpServers` object. **Do not delete other MCP servers you already use.** Replace the placeholder path with the real absolute path to `server.py`.

Fully quit Claude Desktop and reopen it after changing the configuration.

## 5. Confirm the connection

In Claude Desktop, open the tool/connector area near the chat composer and verify that `FlyRank FL-05 Local Evidence` is connected and that the tools are visible.

Do not take the final evidence screenshot yet. First make sure the tools are available.

## 6. Run the three required tasks

Use Claude Desktop and ask it to perform these exact tasks.

### Task 1 — List local files

Prompt:

> Use the FlyRank FL-05 Local Evidence MCP tool to list all files in the demo workspace. Do not answer from the chat context; make the tool call and show the returned file list.

Expected tool:
`list_workspace_files`

Expected files include:
- `project_facts.json`
- `approved_claims.md`
- `sample_notes.txt`

### Task 2 — Read a local file

Prompt:

> Use the FlyRank FL-05 Local Evidence MCP tool to read `approved_claims.md` from the demo workspace. Make the MCP tool call and then summarize the returned content.

Expected tool:
`read_workspace_file`

### Task 3 — Inspect local file metadata

Prompt:

> Use the FlyRank FL-05 Local Evidence MCP tool to inspect `project_facts.json`. Return its file size, line count, and SHA-256 hash from the MCP tool result.

Expected tool:
`get_file_metadata`

## 7. Capture REAL screenshots

Capture three screenshots from Claude Desktop, one after each task.

Each screenshot should clearly show:
- Claude Desktop window.
- The user prompt.
- The MCP/tool call or tool-use indicator.
- The returned result.
- Enough of the server/tool name to prove it is the connected MCP server.

Recommended filenames:
- `evidence/screenshots/01_list_workspace_files.png`
- `evidence/screenshots/02_read_approved_claims.png`
- `evidence/screenshots/03_file_metadata.png`

**Do not create or edit screenshots to make a tool call appear.** The screenshots must be actual captures from your working Claude Desktop session.

## 8. Evidence quality check

Before submission, verify:
- The MCP server name is visible.
- The tool call is visible or otherwise clearly indicated by Claude Desktop.
- The result is visible.
- The three screenshots are different tasks.
- The results match the files in `sample_workspace`.
- No API key, password, token, or private information is visible.

## 9. Final packaging

After the three real screenshots are inside `evidence/screenshots/`, open `docs/EVALUATION_CHECKLIST.md` and mark the evidence item complete.

Then ZIP the **entire project folder**, keeping the folder structure intact.

The ZIP should contain the explainer, code, setup instructions, sample workspace, config example, tests, and the three real screenshots.
