# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        node_map = {}
        curr = head
        dummy = curr1 = RandomListNode(0)
        
        while curr:
            curr1.next = RandomListNode(curr.label)
            node_map[curr] = curr1.next
            curr = curr.next
            curr1 = curr1.next
        
        curr = head
        curr1 = dummy.next        
        while curr:
            if curr.random:
                curr1.random = node_map[curr.random]
            curr, curr1 = curr.next, curr1.next
            
        return dummy.next