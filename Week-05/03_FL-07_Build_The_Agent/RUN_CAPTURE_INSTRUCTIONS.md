# How to record the required raw run capture

The assignment specifically asks for **one raw, unedited screen capture of about 2 minutes** showing the full loop from request to result.

I cannot honestly manufacture that recording because it must show your actual machine/session. Do this once after extracting the ZIP:

1. Open Command Prompt/PowerShell in the project folder.
2. Run:
   `python agent.py`
3. Type these commands during the recording:
   `sources OSI model`
   `explain OSI model`
   `plan 90 Computer Networks Unit 1`
   `status OSI model revised`
   `progress`
4. Keep the recording continuous and unedited.
5. Upload the resulting video/screen capture under **Files** in the FL-07 portal.

If you set `GEMINI_API_KEY`, the `explain` command can use Gemini. Without a key, the local-note fallback still demonstrates the live file connection and the complete end-to-end scripted-agent loop.
