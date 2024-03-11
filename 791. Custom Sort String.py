import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(customSortString("cba", "abcd"), "cbad")
        self.assertEqual(customSortString("bcafg", "abcd"), "bcad")

def customSortString(order: str, s: str) -> str:
    pass


if __name__ == "__main__":
    unittest.main()