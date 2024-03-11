import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(customSortString("cba", "abcd"), "cbad")
        self.assertEqual(customSortString("bcafg", "abcd"), "bcad")

def customSortString(order: str, s: str) -> str:
    print("Hello World")


if __name__ == "__main__":
    unittest.main()