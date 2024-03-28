import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(vals: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = {0: dummy}
    cumulative_sum = 0
    node = head

    while node:
        cumulative_sum += node.val
        if cumulative_sum in prefix_sum:
            prev = prefix_sum[cumulative_sum]
            temp = prev.next
            sum_remove = cumulative_sum
            while temp != node:
                sum_remove += temp.val
                del prefix_sum[sum_remove]
                temp = temp.next
            prev.next = node.next
        else:
            prefix_sum[cumulative_sum] = node
        node = node.next

    return dummy.next

def linkedListToList(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestSolution(unittest.TestCase):
    def test_sol(self):
        testCaseInput = createLinkedList([1, 2, -3, 3, 1])
        result = removeZeroSumSublists(testCaseInput)
        self.assertEqual(linkedListToList(result), [3, 1])

if __name__ == "__main__":
    unittest.main()
    
