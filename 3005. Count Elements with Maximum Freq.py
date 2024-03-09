import unittest

class TestSolution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(maxFrequencyElements([1,2,2,3,1,4]), 4)
        self.assertEqual(maxFrequencyElements([1,2,3,4,5]), 5)

def maxFrequencyElements(nums: list[int]) -> int:
    myDict = {}
    maxFreq = 1
    for num in nums:
        if num in myDict:
            myDict[num] += 1
            maxFreq = max(maxFreq, myDict[num])
        else:
            myDict[num] = 1 

    result = 0
    for key in myDict:
        if myDict[key] == maxFreq:
            result += maxFreq
        
    return result

if __name__ == "__main__":
    unittest.main()