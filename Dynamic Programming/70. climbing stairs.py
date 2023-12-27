import unittest

class testClimbStairs(unittest.TestCase):
    def testBase(self):
        self.assertEqual(climbStairs(0), 0)
        self.assertEqual(climbStairs(1), 1)
        self.assertEqual(climbStairs(2), 2)
    
    def testGeneric(self):
        self.assertEqual(climbStairs(3), 3)
    

def climbStairs(n:int) -> int:
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

if __name__ == "__main__":
    unittest.main()