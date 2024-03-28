import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(findDuplicates([1,3,4,2,2]), 2)
        self.assertEqual(findDuplicates([3,1,3,4,2]), 3)
        self.assertEqual(findDuplicates([3,3,3,3,3]), 3)


def findDuplicates(nums: list[int]) -> int:
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

if __name__ == "__main__":
    unittest.main()