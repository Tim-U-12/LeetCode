import unittest

class TestSolution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(maxFrequencyElements([1,2,2,3,1,4]), 4)
        self.assertEqual(maxFrequencyElements([1,2,3,4,5]), 5)

def maxFrequencyElements(nums: list[int]) -> int:
    myDict = {}
    result = []
    maxFreq = 0

    for num in nums:
        if num in myDict:
            myDict[num] += 1
            if myDict[num] == maxFreq:
                result.append(num)
            elif myDict[num] > maxFreq:
                result = [num]
                maxFreq = myDict[num]
        else:
            myDict[num] = 1
            if myDict[num] == maxFreq:
                result.append(num)
            elif myDict[num] > maxFreq:
                result = [num]
                maxFreq = myDict[num]
        
    return len(result) * maxFreq

if __name__ == "__main__":
    unittest.main()