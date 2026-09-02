#!/usr/bin/env python3
"""
StudyPilot — a small scripted personal study agent.

Core job:
    Search the user's local study notes and help with explanation, quiz,
    revision planning, and simple progress tracking.

Optional AI:
    If GEMINI_API_KEY is present, the agent can use Gemini for richer
    explanations while still grounding the request in retrieved local notes.
    The local-file workflow works without an API key.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Tuple

BASE = Path(__file__).resolve().parent
NOTES_DIR = BASE / "notes"
DATA_DIR = BASE / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"

STOPWORDS = {
    "the","and","for","with","from","this","that","what","which","your","have",
    "about","into","then","give","explain","tell","unit","topic","please","me",
    "how","can","you","are","is","of","to","in","a","an","on","my","i","it"
}

def load_progress() -> Dict[str, str]:
    if not PROGRESS_FILE.exists():
        return {}
    try:
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

def save_progress(progress: Dict[str, str]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2), encoding="utf-8")

def tokenize(text: str) -> List[str]:
    return [x for x in re.findall(r"[a-zA-Z0-9]+", text.lower()) if x not in STOPWORDS and len(x) > 1]

def note_files() -> List[Path]:
    return sorted([p for p in NOTES_DIR.rglob("*") if p.suffix.lower() in {".txt", ".md"}])

def search_notes(query: str, limit: int = 3) -> List[Tuple[Path, str, int]]:
    terms = set(tokenize(query))
    results = []
    for path in note_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            score = sum(1 for t in terms if t in line.lower())
            if score:
                results.append((path, line.strip(), score))
    results.sort(key=lambda x: (-x[2], str(x[0])))
    return results[:limit]

def read_relevant_context(query: str, max_chars: int = 4500) -> str:
    hits = search_notes(query, limit=6)
    if not hits:
        return ""
    chunks = []
    seen = set()
    for path, line, _ in hits:
        if path in seen:
            continue
        seen.add(path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        # Keep a compact section around the first matching term.
        low = text.lower()
        positions = [low.find(t.lower()) for t in tokenize(query) if low.find(t.lower()) >= 0]
        pos = min(positions) if positions else 0
        start = max(0, pos - 500)
        chunks.append(f"[{path.relative_to(BASE)}]\n{text[start:start+1500]}")
        if sum(len(x) for x in chunks) >= max_chars:
            break
    return "\n\n".join(chunks)[:max_chars]

def call_gemini(question: str, context: str) -> str | None:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + key
    prompt = f"""You are StudyPilot, a focused study coach.
Use the user's local notes below as the primary source.
If the notes do not support a syllabus-specific claim, explicitly say that.
Explain clearly for a BCA student. Do not invent teacher instructions.

USER REQUEST:
{question}

LOCAL NOTES:
{context or "(No relevant local notes were found.)"}
"""
    body = json.dumps({"contents":[{"parts":[{"text":prompt}]}]}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type":"application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception:
        return None

def grounded_explanation(question: str) -> str:
    context = read_relevant_context(question)
    ai = call_gemini(question, context)
    if ai:
        return ai + "\n\nSource: local notes + Gemini (API key configured)."
    if not context:
        return ("I could not find supporting material in the local notes. "
                "I will not pretend the information came from your notes. "
                "Add the relevant note file and try again.")
    # No-key fallback: give a transparent, useful extraction.
    return ("I found relevant material in your local notes. Here is the grounded "
            "excerpt to study:\n\n" + context +
            "\n\nAI mode is not configured, so this run is using the local-note "
            "fallback. Set GEMINI_API_KEY if you want model-generated explanations.")

def make_quiz(topic: str, count: int = 5) -> List[str]:
    context = read_relevant_context(topic, max_chars=6000)
    if not context:
        return []
    # Extract headings/short factual lines as simple question seeds.
    lines = [x.strip() for x in context.splitlines() if x.strip()]
    seeds = []
    for line in lines:
        if len(line) < 120 and (":" in line or line.startswith("#") or re.match(r"^\d+[\).\s]", line)):
            clean = re.sub(r"^#+\s*", "", line)
            if clean not in seeds:
                seeds.append(clean)
    questions = []
    for seed in seeds[:count]:
        questions.append(f"Explain or define: {seed}")
    while len(questions) < count:
        questions.append(f"Write a short exam answer about {topic} using your notes.")
    return questions[:count]

def revision_plan(topic: str, minutes: int) -> str:
    if minutes <= 0:
        return "Time must be greater than zero minutes."
    hits = search_notes(topic, limit=8)
    if not hits:
        return "I could not find that topic in the local notes, so I will not invent a syllabus-specific plan."
    blocks = []
    remaining = minutes
    suggested = [
        ("Quick scan of the notes", max(10, int(minutes*0.15))),
        ("Understand the main concepts", max(15, int(minutes*0.35))),
        ("Active recall / write key points", max(10, int(minutes*0.25))),
        ("Exam-style practice", max(10, int(minutes*0.20))),
    ]
    total = sum(x[1] for x in suggested)
    if total > minutes:
        scale = minutes / total
        suggested = [(name, max(5, int(t*scale))) for name,t in suggested]
    total = sum(t for _,t in suggested)
    suggested[-1] = (suggested[-1][0], suggested[-1][1] + minutes-total)
    for idx, (name, mins) in enumerate(suggested, 1):
        blocks.append(f"{idx}. {name} — {mins} min")
    return f"Revision plan for **{topic}** ({minutes} minutes):\n" + "\n".join(blocks)

def set_status(topic: str, status: str) -> str:
    allowed = {"not started", "learning", "revised"}
    if status not in allowed:
        return "Status must be: not started, learning, or revised."
    progress = load_progress()
    progress[topic] = status
    save_progress(progress)
    return f"Saved progress: {topic} → {status}"

def get_progress() -> str:
    progress = load_progress()
    if not progress:
        return "No study progress has been saved yet."
    return "\n".join(f"- {k}: {v}" for k,v in sorted(progress.items()))

def print_help() -> None:
    print("""
Commands:
  explain <topic/question>       Explain using local notes
  quiz <topic>                   Generate 5 practice questions
  plan <minutes> <topic>         Make a time-boxed revision plan
  status <topic> <state>         Save: not started | learning | revised
  progress                       Show saved study progress
  sources <topic>                Show matching local-note files/lines
  help                           Show this help
  exit                           Quit

Example:
  explain OSI model
  quiz Computer Networks Unit 1
  plan 90 Computer Networks Unit 1
  status OSI model revised
""")

def handle(command: str) -> bool:
    if not command.strip():
        return True
    parts = command.strip().split()
    cmd = parts[0].lower()
    if cmd in {"exit","quit"}:
        return False
    if cmd == "help":
        print_help()
    elif cmd == "explain":
        q = command.partition(" ")[2]
        print("\n" + grounded_explanation(q) + "\n")
    elif cmd == "quiz":
        topic = command.partition(" ")[2]
        qs = make_quiz(topic)
        if not qs:
            print("No supporting notes found.")
        else:
            print("\nQuiz:")
            for i,q in enumerate(qs,1):
                print(f"{i}. {q}")
            print()
    elif cmd == "plan":
        if len(parts) < 3:
            print("Usage: plan <minutes> <topic>")
        else:
            try:
                mins = int(parts[1])
                topic = " ".join(parts[2:])
                print("\n" + revision_plan(topic, mins) + "\n")
            except ValueError:
                print("Minutes must be a number.")
    elif cmd == "status":
        if len(parts) < 3:
            print("Usage: status <topic> <not started|learning|revised>")
        else:
            # Last token is status; everything before it is topic.
            status = parts[-1].lower()
            topic = " ".join(parts[1:-1])
            print(set_status(topic, status))
    elif cmd == "progress":
        print("\n" + get_progress() + "\n")
    elif cmd == "sources":
        q = command.partition(" ")[2]
        hits = search_notes(q, limit=10)
        if not hits:
            print("No matching note lines found.")
        else:
            for path,line,score in hits:
                print(f"- {path.relative_to(BASE)} (score {score}): {line}")
    else:
        print("Unknown command. Type 'help'.")
    return True

def main() -> None:
    print("="*58)
    print("StudyPilot — Personal BCA Study Coach")
    print("Local-note grounded scripted agent")
    print("="*58)
    print(f"Notes connected: {len(note_files())} local file(s)")
    print("AI model: " + ("Gemini enabled" if os.getenv("GEMINI_API_KEY") else "local fallback"))
    print("Type 'help' for commands.\n")
    while True:
        try:
            command = input("StudyPilot> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not handle(command):
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
