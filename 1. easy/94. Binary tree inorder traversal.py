import unittest

# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    head = root

    visited = []
    def dfs(head):
        if head in visited or head is None:
            return []
        
        visited.append(head)

        left = dfs(head.left)
        right = dfs(head.right)

        return left + [head.val] + right
        
    return dfs(head)

class TestSolution(unittest.TestCase):
    def test_sol(self):
        # test 1
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual(inorderTraversal(root), [1,3,2])
        # test 2
        root = TreeNode()
        self.assertEqual(inorderTraversal(root), [])
        # test 3
        root = TreeNode(1)
        self.assertEqual(inorderTraversal(root), [1])

if __name__ == "__main__":
    unittest.main()