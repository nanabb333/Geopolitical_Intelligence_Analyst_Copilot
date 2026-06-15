import re
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from generate_brief import generate_brief  # noqa: E402


class TestGenerateBrief(unittest.TestCase):
    def test_generated_brief_contains_required_sections(self):
        brief = generate_brief("US announces a new semiconductor subsidy package.", top_k=3)

        required_sections = [
            "## User Event Description",
            "## Event Classification",
            "## Most Similar Historical Events",
            "## Historical Market Reactions",
            "## Potential Future Pathways",
            "## Key Risks and Uncertainties",
            "## Executive Brief",
        ]
        for section in required_sections:
            self.assertIn(section, brief)

    def test_generated_brief_contains_safety_language(self):
        brief = generate_brief("US announces a new semiconductor subsidy package.", top_k=3)

        self.assertIn("not a forecast", brief)
        self.assertIn("not a", brief)
        self.assertIn("investment recommendation", brief)
        self.assertIn("supports research and strategic analysis only", brief)

    def test_generated_brief_avoids_recommendation_and_probability_claims(self):
        brief = generate_brief("US announces a new semiconductor subsidy package.", top_k=3)

        prohibited_patterns = [
            r"\bbuy\b",
            r"\bsell\b",
            r"\bhold\b",
            r"\bprice target\b",
            r"\bexpected return\b",
            r"\b\d+(\.\d+)?%\s+(chance|likelihood|probability)\b",
        ]
        for pattern in prohibited_patterns:
            self.assertIsNone(re.search(pattern, brief, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
