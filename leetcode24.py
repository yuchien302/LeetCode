# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        cur, new_head = head, head.next
        cur.next.next, cur.next = cur, self.swapPairs(cur.next.next)
        
        return new_head