import unittest

class TestFindJudge(unittest.TestCase):
    def testFindJudge(self) -> None:
        self.assertEqual(findJudge(3, [[1,3],[2,3]]), 3)
        self.assertEqual(findJudge(3, [[1,3],[2,3],[3,1]]), -1)

def findJudge(n:int, trust: list[list[int]]) -> int:
    suspects = [[0 for _ in range(n)] for _ in range(n)]

    for t in trust:
        suspects[t[0] - 1][t[1] - 1] = 1

    print(suspects)

    town_judge = []
    for i in range(n):
        count = 0
        for j in range(n):
            count += suspects[j][i]
        if count == n - 1 and sum(suspects[i]) == 0:
            town_judge.append(i + 1)

    if len(town_judge) == 1:
        return town_judge[0]
    else:
        return -1
        
if __name__ == "__main__":
    unittest.main()