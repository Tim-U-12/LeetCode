import unittest

class TestSolution(unittest.TestCase):
    def test_sol(self):
        self.assertEqual(customSortString("cba", "abcd"), "cbad")
        self.assertEqual(customSortString("bcafg", "abcd"), "bcad")

def customSortString(order: str, s: str) -> str:
    sol = ""
    myDict = {}
    for letter in s:
        if letter in myDict:
            myDict[letter] += 1
        else:
            myDict[letter] = 1
    
    for letter in order:
        if letter in myDict:
            sol += (myDict[letter] * letter)
            del myDict[letter]
    
    for key in myDict:
        sol += (myDict[key] * key)
    
    print(sol)
    return sol



if __name__ == "__main__":
    unittest.main()