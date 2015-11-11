# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        stack = []
        while fast:
            if not fast.next:
                slow = slow.next
                break
            
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        if not stack:
            return True
            
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True