import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(countGoodSubstrings("xyzzaz"), 1)
        self.assertEqual(countGoodSubstrings("aababcabc"), 4)

def countGoodSubstrings(s:str) -> int:
    count = 0

    for i in range(len(s) - 2):
        if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
            count += 1

    return count

if __name__ == "__main__":
    unittest.main()