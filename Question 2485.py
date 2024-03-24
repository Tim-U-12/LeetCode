import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(pivotInteger(8), 6)
        self.assertEqual(pivotInteger(1), 1)
        self.assertEqual(pivotInteger(4), -1)

def pivotInteger(n: int) -> int:
    start = 1
    end = n

    sum_left = 1
    sum_right = n 

    while start < end:
        if sum_left < sum_right:
            start += 1
            sum_left += start
        else:
            end -= 1
            sum_right += end
    
    if sum_left != sum_right:
        return -1
    
    return end

if __name__ == "__main__":
    unittest.main()