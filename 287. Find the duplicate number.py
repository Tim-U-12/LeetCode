import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(findDuplicates([1,3,4,2,2]), [1, 2, 2, 3, 4])

def findDuplicates(nums: list[int]):
    n = len(nums)
    sorted_index = 0

    for i in range(n):
        smallest_val_index = i
        for j in range(i, n):
            if nums[j] < nums[smallest_val_index]:
                smallest_val_index = j
        nums[sorted_index], nums[smallest_val_index] = nums[smallest_val_index], nums[sorted_index]
        sorted_index += 1

    return nums

if __name__ == "__main__":
    unittest.main()