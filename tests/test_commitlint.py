import unittest
from commitlint_tr import lint

class TestLint(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(lint("feat: add new parser"), [])
        self.assertEqual(lint("fix(parser): handle empty input"), [])
    def test_invalid_type(self):
        assert any("unknown type" in i for i in lint("unknown: something"))
    def test_missing_colon(self):
        assert len(lint("feat something")) > 0
    def test_capital_desc(self):
        assert any("capital" in i for i in lint("feat: Add new parser"))
    def test_empty(self):
        assert len(lint("")) > 0

if __name__ == "__main__":
    unittest.main()
