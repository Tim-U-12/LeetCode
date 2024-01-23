import unittest

class TestRob(unittest.TestCase):
    def testRob(self):
        self.assertEqual(rob([1,2,3,1]), 4)
        self.assertEqual(rob([2,7,9,3,1]), 12)
        self.assertEqual(rob([2,1,1,2]), 4)
        self.assertEqual(rob([1,7,9,2]), 10)

def rob(nums: list[int]) -> int:
    n = len(nums)

    if n <= 2: return max(nums)
    
    temp = nums[0]
    sol = max(nums[0], nums[1])

    for i in range(2, n):
        temp, sol = sol, max(sol, nums[i] + temp)

    return sol   
 
if __name__ == "__main__":
    unittest.main()