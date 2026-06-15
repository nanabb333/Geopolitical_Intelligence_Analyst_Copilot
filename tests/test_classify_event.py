import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from classify_event import classify_event  # noqa: E402


class TestClassifyEvent(unittest.TestCase):
    def test_semiconductor_subsidy_classification_is_deterministic(self):
        event = classify_event("US announces a new semiconductor subsidy package.")

        self.assertEqual(event.event_type, "support")
        self.assertEqual(event.policy_subtype, "subsidy_award")
        self.assertEqual(event.country_or_region, "US")
        self.assertEqual(event.sector, "semiconductors")
        self.assertGreaterEqual(event.state_support, 1)

    def test_export_control_classification_is_deterministic(self):
        event = classify_event(
            "The United States announces new export controls on advanced AI chips and semiconductor manufacturing equipment."
        )

        self.assertEqual(event.event_type, "threat_contrast")
        self.assertEqual(event.policy_subtype, "export_control")
        self.assertEqual(event.country_or_region, "US")
        self.assertIn(event.sector, {"semiconductors", "AI chips"})
        self.assertGreaterEqual(event.threat_signal, 1)


if __name__ == "__main__":
    unittest.main()
