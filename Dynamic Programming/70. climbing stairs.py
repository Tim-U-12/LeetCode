import unittest

class testClimbStairs(unittest.TestCase):
    def testBase(self):
        self.assertEqual(bottomUpClimbStairs(0), 0)
        self.assertEqual(bottomUpClimbStairs(1), 1)
        self.assertEqual(bottomUpClimbStairs(2), 2)
    
    def testGeneric(self):
        self.assertEqual(bottomUpClimbStairs(3), 3)

    def testTopDown(self):
        self.assertEqual(topDownClimbStairs(3), 3)

    

def bottomUpClimbStairs(n:int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case default:
            result = [0] * (n+1)
            result[1] = 1
            result[2] = 2

            for i in range(3, n + 1):
                result[i] = result[i - 2] + result[i - 1]

            return result[n]

def topDownClimbStairs(n:int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n < 0:
        return 0
    
    return topDownClimbStairs(n - 1) + topDownClimbStairs(n - 2)

if __name__ == "__main__":
    unittest.main()