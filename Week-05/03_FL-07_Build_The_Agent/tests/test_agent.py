import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import agent

class TestStudyPilot(unittest.TestCase):
    def test_note_search(self):
        hits = agent.search_notes("OSI model")
        self.assertTrue(hits)
        self.assertTrue(any("OSI" in line for _, line, _ in hits))

    def test_missing_topic_is_not_fabricated(self):
        answer = agent.grounded_explanation("quantum archaeology of mars")
        self.assertIn("could not find", answer.lower())

    def test_revision_plan(self):
        plan = agent.revision_plan("Computer Networks Unit 1", 90)
        self.assertIn("90 minutes", plan)
        self.assertIn("Revision plan", plan)

    def test_progress_roundtrip(self):
        with TemporaryDirectory() as d:
            old_file, old_dir = agent.PROGRESS_FILE, agent.DATA_DIR
            try:
                agent.PROGRESS_FILE = Path(d) / "progress.json"
                agent.DATA_DIR = Path(d)
                msg = agent.set_status("OSI model", "revised")
                self.assertIn("revised", msg)
                self.assertIn("OSI model", agent.get_progress())
            finally:
                agent.PROGRESS_FILE, agent.DATA_DIR = old_file, old_dir

    def test_quiz(self):
        qs = agent.make_quiz("Computer Networks Unit 1")
        self.assertEqual(len(qs), 5)

if __name__ == "__main__":
    unittest.main()
