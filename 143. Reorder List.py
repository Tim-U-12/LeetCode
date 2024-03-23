import unittest

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def reorderList(head) -> None:
    pointer = head
    nodes = []

    while pointer:
        nodes.append(pointer)
        pointer = pointer.next

class TestSolution(unittest.TestCase):
    def test_sol(self):
        pass

if __name__ == "__main__":
    unittest.main()

