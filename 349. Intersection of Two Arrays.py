import unittest

class TestSolution(unittest.TestCase):
    def test_solution(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        self.assertEqual(intersection(nums1, nums2), [2])

        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        self.assertEqual(intersection(nums1, nums2), [9, 4])


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)

    if len(nums1) < len(nums2):
        return search(nums1, nums2)
    return search(nums2, nums1)

def search(nums1, nums2):
    sol = []
    for num in nums1:
        if num in nums2:
                sol.append(num)
    return sol
        

if __name__ == "__main__":
    unittest.main()