# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        has_cycle = False
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            
            if fast == slow:
                has_cycle = True
                break
            
        if not has_cycle:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow, slow2 = slow.next, slow2.next
            
        return slow
            
            
            