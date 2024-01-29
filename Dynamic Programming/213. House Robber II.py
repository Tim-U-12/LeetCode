import unittest

class TestRob(unittest.TestCase):
    def testGeneric(self):
        self.assertEqual(rob([2,3,2]), 3)
        self.assertEqual(rob([1,2,3,1]), 4)
        self.assertEqual(rob([1,2,3]), 3)
        self.assertEqual(rob([6,6,4,8,4,3,3,10]), 27)

def rob(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return max(nums)
    
    temp = nums[0]
    potential_sol_one = max(nums[0], nums[1])

    for i in range(2, n - 1):
        temp, potential_sol_one = potential_sol_one, max(temp + nums[i], potential_sol_one)
    
    temp_two = nums[1]
    potential_sol_two = max(nums[1], nums[2])
    for i in range(3, n):
        temp_two, potential_sol_two = potential_sol_two, max(temp_two + nums[i], potential_sol_two)
    
    return max(potential_sol_two, potential_sol_one)

    
if __name__ == "__main__":
    unittest.main()