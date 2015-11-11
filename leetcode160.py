# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        n1, n2 = headA, headB
        count = 0
        while n1 != n2:
            if n1:
                n1 = n1.next
            else: 
                n1 = headB
                
            if n2:
                n2 = n2.next
            else: 
                n2 = headA
        return n1
            
        
        