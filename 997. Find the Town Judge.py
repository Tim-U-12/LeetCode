import unittest

class TestFindJudge(unittest.TestCase):
    def testFindJudge(self) -> None:
        self.assertEqual(findJudge(3, [[1,3],[2,3]]), 3)

def findJudge(n:int, trust: list[list[int]]) -> int:
    # The town judge trusts nobody.
    suspects = [[True for _ in range(n)] for _ in range(n)]
    
    for t in trust:
        print(t)
        suspects[t[0] - 1][t[1] - 1] = False
    
    result = []
    for i, row in enumerate(suspects):
        if len(set(row)) == 1:
            result.append(i)
    
    if len(result) == 1:
        return result[0] + 1
    else:
        return -1




if __name__ == "__main__":
    unittest.main()