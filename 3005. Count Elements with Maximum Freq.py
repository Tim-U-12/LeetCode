import unittest

class TestSolution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(maxFrequencyElements([1,2,2,3,1,4]), 2)

def maxFrequencyElements(nums: list[int]) -> int:
    myDict = {}
    maxFreq = 1
    for num in nums:
        if num in myDict:
            maxFreq = max(maxFreq, myDict[num] + 1)
        else:
            myDict[num] = 1 

    return maxFreq

if __name__ == "__main__":
    unittest.main()