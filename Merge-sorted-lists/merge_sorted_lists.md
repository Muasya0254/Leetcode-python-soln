# Merge Two Sorted Lists

This Python script implements a solution for merging two sorted linked lists. The merged list is created by splicing together the nodes of the first two lists. The solution is designed for the problem described on [LeetCode - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/21).

## Usage

To use the `mergeTwoLists` function, you can follow these steps:

1. Define the `ListNode` class to represent a singly-linked list node.
2. Create instances of the `ListNode` class to represent the input sorted linked lists.
3. Call the `mergeTwoLists` function with the two linked lists as arguments.

Example usage:

```python
# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Call the mergeTwoLists function
result = mergeTwoLists(list1, list2)
