import unittest

class TreeNode():
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = self.left
        self.right = right

def isSymmetric(root) -> bool:
    if not root:
        return True
    
    def isMirror(t1, t2):
        if  not t1 or not t2:
            return t1 == t2
        if t1.val != t2.val:
            return False
        
        return isMirror(t1.left, t2.right) and isMirror(t1.left, t2.right)
    return isMirror(root.left, root.right)

class TestSolution(unittest.main()):
    def test_sol(self):
        pass

if __name__ == "__main__":
    unittest.main()