import unittest

class TestMinCostClimbingStairs(unittest.TestCase):
    def testBottomUpMinCostClimbingStairs(self):
        self.assertEqual(BottomUpMinCostClimbingStairs([10,15,20]), 15)
        self.assertEqual(BottomUpMinCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]), 6)

    def testTopDownMinCostClimbingStairs(self):
        pass

def BottomUpMinCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)

    if n <= 2:
        return min(cost)

    first, second = cost[0], cost[1]

    for i in range(2, n):
        current = cost[i] + min(first, second)
        first, second = second, current
    
    return min(first, second)


if __name__ == "__main__":
    unittest.main()