import re
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from generate_workbench_report import generate_workbench_report  # noqa: E402


class TestGenerateWorkbenchReport(unittest.TestCase):
    def test_workbench_report_contains_required_sections(self):
        report = generate_workbench_report("US announces a new semiconductor subsidy package.", top_k=3)

        required_sections = [
            "## A. Scenario Classification",
            "## B. Historical Analogues",
            "## C. Market Reaction Comparison",
            "## D. Observed Pathways",
            "## E. Executive Memo",
            "### Export Package",
        ]
        for section in required_sections:
            self.assertIn(section, report)

    def test_workbench_report_preserves_safety_boundaries(self):
        report = generate_workbench_report("US announces a new semiconductor subsidy package.", top_k=3)

        self.assertIn("not a forecast", report)
        self.assertIn("investment recommendation", report)
        prohibited_patterns = [
            r"\bbuy\b",
            r"\bsell\b",
            r"\bhold\b",
            r"\bprice target\b",
            r"\bexpected return\b",
            r"\b\d+(\.\d+)?%\s+(chance|likelihood|probability)\b",
        ]
        for pattern in prohibited_patterns:
            self.assertIsNone(re.search(pattern, report, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
