import unittest

class TestTribonacci(unittest.TestCase):
    def testBottomUp(self):
        self.assertEqual(bottomUpTribonacci(0), 0)
        self.assertEqual(bottomUpTribonacci(1), 1)
        self.assertEqual(bottomUpTribonacci(3), 2)
        self.assertEqual(bottomUpTribonacci(4), 4)
        self.assertEqual(bottomUpTribonacci(25), 1389537)

    def testTopDown(self):
        self.assertEqual(topDownTribonacci(0), 0)
        self.assertEqual(topDownTribonacci(1), 1)
        self.assertEqual(topDownTribonacci(3), 2)
        self.assertEqual(topDownTribonacci(4), 4)
        self.assertEqual(topDownTribonacci(25), 1389537)

def bottomUpTribonacci(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1 | 2:
            return 1
        case _:
            first_previous = 0
            second_previous = 1
            third_previous = 1

            for _ in range(3, n + 1):
                tribonacci_number = first_previous + second_previous + third_previous
                first_previous, second_previous, third_previous = second_previous, third_previous, tribonacci_number
            
            return tribonacci_number

def topDownTribonacci(n: int) -> int:
    memo = {0: 0, 1: 1, 2: 1}

    def rec(n: int) -> int:
        if n in memo:
            return memo[n]
        return rec(n - 1) + rec(n - 2) + rec(n - 3)
    return rec(n)

if __name__ == "__main__":
    unittest.main()
