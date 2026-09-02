# FL-07 Build Log — StudyPilot

## Build 1 — Core skeleton
- Created a Python scripted agent around one focused job: studying from local notes.
- Added a `notes/` folder as the live data connection.
- Added command routing for explain, quiz, plan, status, progress, and sources.

## Build 2 — Grounding
- Added local note search before explanation.
- Added a missing-information rule so the agent does not pretend unsupported information came from the notes.
- Added a transparent local fallback when no model API key is configured.

## Build 3 — Agent memory/progress
- Added a small JSON progress store.
- Added explicit statuses: `not started`, `learning`, `revised`.
- Kept destructive operations out of the MVP.

## Build 4 — Evaluation
- Added five automated tests covering:
  1. live note search,
  2. missing-information handling,
  3. time-boxed planning,
  4. progress save/read,
  5. quiz generation.
- Added a manual run sequence for the required raw screen capture.

## Deliberate cuts from the FL-06 spec
- External calendar/email connectors were not added because they are not needed for the narrow study-coach MVP.
- Automatic destructive file editing was not added because it increases risk without helping the core job.
- A full web dashboard was cut from this checkpoint to keep the core job runnable within the planned 10-hour scope.

## Important honesty note
The build is intentionally small. The live connection in this checkpoint is the local `notes/` data source. The required raw run capture is not fabricated; it must be recorded from the actual running agent.
