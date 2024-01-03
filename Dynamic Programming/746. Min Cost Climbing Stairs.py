import unittest

class TestMinCostClimbingStairs(unittest.TestCase):
    def testBottomUpMinCostClimbingStairs(self):
        self.assertEqual(BottomUpMinCostClimbingStairs([10,15,20]), 15)
        self.assertEqual(BottomUpMinCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]), 6)

    def testTopDownMinCostClimbingStairs(self):
        pass

def BottomUpMinCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)

    if n == 2:
        return min(cost)

    cache = [float('inf') for _ in range(n)]
    cache[0], cache[1] = cost[0], cost[1]

    for i in range(2, n):
        cache[i] = min(cost[i] + cache[i-1], cost[i] + cache[i-2])
    
    return min(cache[-1], cache[-2])


if __name__ == "__main__":
    unittest.main()