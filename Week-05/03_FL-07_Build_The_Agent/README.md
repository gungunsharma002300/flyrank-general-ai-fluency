# FlyRank FL-07 — Build the Agent

## Agent
**StudyPilot — Personal BCA Study Coach**

This is a working Python scripted-agent MVP based on the FL-06 design.

### Core job
Use the user's own local study notes to:
- explain topics,
- generate quiz questions,
- make time-boxed revision plans,
- save simple study progress.

### Live connection
The agent reads the `notes/` directory at runtime. This is the required live file/data connection.

### Optional AI model
Set `GEMINI_API_KEY` in the environment to enable Gemini-generated explanations grounded in retrieved local notes. The project still runs without the key using a transparent local-note fallback.

## Run

```bash
python agent.py
```

Then:
```text
sources OSI model
explain OSI model
plan 90 Computer Networks Unit 1
status OSI model revised
progress
```

## Test

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Submission package

- `agent.py` — working agent
- `notes/demo_notes.md` — connected local data source
- `data/progress.json` — local progress store
- `tests/test_agent.py` — evaluation tests
- `BUILD_LOG.md` — iteration/build record
- `RUN_CAPTURE_INSTRUCTIONS.md` — how to record the required raw capture
- `FL07_SUBMISSION_NOTES.md` — portal Notes text
- `FL07_CHECKLIST.md` — requirement checklist

No fake screenshot/video or fake public URL is included.
