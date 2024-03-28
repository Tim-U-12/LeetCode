import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(findMaxLength([0,1]), 2)
        self.assertEqual(findMaxLength([0,1, 0]), 2)

def findMaxLength(nums: list[int]) -> int:
    count_index = {0: -1}
    max_length = count = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count in count_index:
            max_length = max(max_length, i - count_index[count])
        else:
            count_index[count] = i

    return max_length

if __name__ == "__main__":
    unittest.main()