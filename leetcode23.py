# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        dummy = ListNode(0)
        node = dummy
        
        [heappush(h, (n.val, n)) for n in lists if n]
            
            
        while len(h) != 0:
            (val, n) = heappop(h)
            node.next = ListNode(val)
            node = node.next
            if n.next:
                heappush(h, (n.next.val, n.next))
                
        return dummy.next
        
        