import unittest
from linked_list_cycle import Solution, ListNode

class TestSolution(unittest.TestCase):

    def test_has_cycle_with_cycle(self):
        # Create a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next  # Creating a cycle

        solution = Solution()
        result = solution.hasCycle(head)
        self.assertTrue(result)

    def test_has_cycle_no_cycle(self):
        # Create a linked list without a cycle: 1 -> 2 -> None
        head = ListNode(1)
        head.next = ListNode(2)

        solution = Solution()
        result = solution.hasCycle(head)
        self.assertFalse(result)

    def test_has_cycle_single_node(self):
        # Create a linked list with a single node: 1 -> None
        head = ListNode(1)

        solution = Solution()
        result = solution.hasCycle(head)
        self.assertFalse(result)

    def test_has_cycle_cycle_at_beginning(self):
        # Create a linked list with a cycle at the beginning: 1 -> 2 -> 3 -> 1 (cycle)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head  # Creating a cycle

        solution = Solution()
        result = solution.hasCycle(head)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
