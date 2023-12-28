# Linked List Cycle Detection

This README provides an overview of the solution to the problem of detecting cycles in a linked list.

## Problem Description

Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. The index of the node where the tail's next pointer is connected is denoted by 'pos'. Note that 'pos' is not passed as a parameter.

The function should return `true` if there is a cycle in the linked list, and `false` otherwise.

## Example

### Example 1

```markdown
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2

```markdown
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3

```markdown
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
```

## Approach

The problem can be solved using Floyd's Tortoise and Hare algorithm, where two pointers move at different speeds through the linked list. If there is a cycle, the two pointers will eventually meet at some point.

## Implementation

The solution is implemented in a programming language of your choice. The code file, e.g., `LinkedListCycleDetection.py` (replace with the appropriate file extension for your programming language), contains the implementation of the algorithm.

## How to Use

To use the solution, follow these steps:

1. Include the implementation file in your project.
2. Call the function with the head of the linked list as the argument.

```python
from LinkedListCycleDetection import has_cycle

# Example Usage
head = create_linked_list([3, 2, 0, -4], 1)  # Create a linked list with a cycle
result = has_cycle(head)
print(result)  # Output: True
