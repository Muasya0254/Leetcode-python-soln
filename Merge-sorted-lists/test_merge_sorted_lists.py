import unittest
from merge_sorted_lists import mergeTwoLists, ListNode   

class TestMergeTwoLists(unittest.TestCase):
    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_merge_two_lists(self):
        # Test Case 1
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 4])
        result = mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

        # Test Case 2
        list1 = self.create_linked_list([])
        list2 = self.create_linked_list([])
        result = mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [])

        # Test Case 3
        list1 = self.create_linked_list([])
        list2 = self.create_linked_list([0])
        result = mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(result), [0])

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
