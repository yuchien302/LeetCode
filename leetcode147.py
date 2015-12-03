# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        dummy = curr = ListNode(0)
        for a in arr:
            curr.next = ListNode(a)
            curr = curr.next
        return dummy.next
        

