# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        else:
            fast  = head
            slow = head

            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
                
                if fast == None or fast.next == None:
                    return False
                elif fast == slow:
                    break

            return False
        