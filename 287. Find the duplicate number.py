import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(findDuplicates([1,3,4,2,2]), 2)
        #self.assertEqual(findDuplicates([3,1,3,4,2]), 3)
        #self.assertEqual(findDuplicates([3,3,3,3,3]), 3)


def findDuplicates(nums: list[int]) -> int:
    n = len(nums)
    sorted_index = 0

    for i in range(n):
        smallest_val_index = i
        for j in range(i, n):
            if nums[j] < nums[smallest_val_index]:
                smallest_val_index = j
        
        if sorted_index > 0 and nums[sorted_index - 1] == nums[smallest_val_index]:
            return nums[sorted_index - 1]
        
        nums[sorted_index], nums[smallest_val_index] = nums[smallest_val_index], nums[sorted_index]
        sorted_index += 1

    return -1

if __name__ == "__main__":
    unittest.main()