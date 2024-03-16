import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(findMaxLength([0,1]), 2)
        self.assertEqual(findMaxLength([0,1, 0]), 2)

def findMaxLength(nums: list[int]) -> int:
    def helper(subarray: list[int]) -> bool:
        zeroes = 0

        for num in subarray:
            if num == 0:
                zeroes += 1
        
        return len(subarray) - zeroes == zeroes

    n = len(nums)

    for i in range(n - 1, -1, -1):
        for j in range(n - i):
            temp = nums[j:j + i + 1]

            if helper(temp):
                return len(temp)
    
    return 0
    
if __name__ == "__main__":
    unittest.main()