# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbersWithC(self, c, l1, l2):
        if l1 is None and l2 is None:
            if c != 0:
                return ListNode(c)
            else:
                return None

        v1 = 0 if l1 is None else l1.val
        v2 = 0 if l2 is None else l2.val
        
        l3 = ListNode((v1 + v2 + c) % 10)
        c = (v1 + v2 + c) // 10
        
        next1 = l1 if l1 is None else l1.next
        next2 = l2 if l2 is None else l2.next
        
        l3.next = self.addTwoNumbersWithC(c, next1, next2)
            
        return l3
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersWithC(0, l1, l2)
                
            
            
            
            