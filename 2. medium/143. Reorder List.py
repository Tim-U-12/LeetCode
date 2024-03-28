import unittest

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def reorderList(head) -> None:
    if not head:
        return None

    current = head
    nodes = []

    while current:
        nodes.append(current)
        current = current.next
    
    current = head
    start = 1
    end = len(nodes) - 1
    end_i = False

    for _ in range(len(nodes) - 1):
        if end_i:
            current.next = nodes[start]
            start += 1
        else:
            current.next = nodes[end]
            end -= 1
        end_i = not end_i
        current = current.next

    current.next = None
    return head

def createLinkedList(node_vals):
    if not node_vals:
        return None
    
    head = ListNode(node_vals[0])
    current = head

    for val in node_vals[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def displayLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    
    return result

class TestSolution(unittest.TestCase):
    def test_sol(self):
        node_vals = [1, 2, 3, 4]
        head = createLinkedList(node_vals)
        sol = reorderList(head)
        self.assertEqual(displayLinkedList(sol), [1, 4, 2, 3])

if __name__ == "__main__":
    unittest.main()