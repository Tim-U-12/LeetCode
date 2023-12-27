import unittest

class testFibonacci(unittest.TestCase):
    def testBottomUp(self):
        self.assertEqual(bottomUpFibonacci(2), 1)
        self.assertEqual(bottomUpFibonacci(3), 2)
        self.assertEqual(bottomUpFibonacci(4), 3)
    
    def testTopDown(self):
        self.assertEqual(topDownFibonacci(0), 0)
        self.assertEqual(topDownFibonacci(1), 1)
        self.assertEqual(topDownFibonacci(2), 1)
        self.assertEqual(topDownFibonacci(3), 2)
        self.assertEqual(topDownFibonacci(4), 3)

def bottomUpFibonacci(n:int) -> int:
    prev = 0
    result = 1

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    for _ in range(n - 1):
        prev, result = result, prev + result

    return result

def topDownFibonacci(n:int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return topDownFibonacci(n - 1) + topDownFibonacci(n - 2)


if __name__ == "__main__":
    unittest.main()