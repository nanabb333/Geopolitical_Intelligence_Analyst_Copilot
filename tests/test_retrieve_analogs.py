import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from retrieve_analogs import retrieve_analogs  # noqa: E402


class TestRetrieveAnalogs(unittest.TestCase):
    def test_retrieval_returns_matching_support_analogs(self):
        _, analogs = retrieve_analogs("US announces a new semiconductor subsidy package.", top_k=5)

        self.assertGreater(len(analogs), 0)
        self.assertTrue(any(analog.event["event_type"] == "support" for analog in analogs))
        self.assertTrue(all(0 <= analog.similarity_score <= 100 for analog in analogs))

    def test_retrieval_returns_matching_export_control_analogs(self):
        _, analogs = retrieve_analogs(
            "The United States announces new export controls on advanced AI chips and semiconductor manufacturing equipment.",
            top_k=5,
        )

        self.assertGreater(len(analogs), 0)
        self.assertTrue(any(analog.event["policy_subtype"] == "export_control" for analog in analogs))
        self.assertTrue(all(analog.score_breakdown for analog in analogs))


if __name__ == "__main__":
    unittest.main()
