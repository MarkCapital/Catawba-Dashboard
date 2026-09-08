import unittest
from pathlib import Path


INDEX = Path(__file__).resolve().parents[1] / "index.html"


def function_body(source: str, name: str, next_marker: str | None = None) -> str:
    start = source.index(f"function {name}(){{")
    end = source.index(next_marker, start) if next_marker else len(source)
    return source[start:end]


class PrintSummaryAppaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = INDEX.read_text()

    def test_month_print_formats_missing_appa_as_na(self):
        body = function_body(self.source, "printSummary")
        self.assertIn("mo.appa == null ? 'N/A' : mo.appa.toFixed(2)", body)
        self.assertNotIn("pCard('Avg APPA score', mo.appa.toFixed(2))", body)

    def test_ytd_print_formats_missing_month_appa_as_na(self):
        body = function_body(self.source, "printYTD", "// ── COLLAPSIBLE SECTIONS")
        self.assertIn("m.appa == null ? 'N/A' : m.appa.toFixed(2)", body)
        self.assertNotIn("${m.appa.toFixed(2)}", body)


if __name__ == "__main__":
    unittest.main()
