# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        arr = []
        while head:
            arr.append(head)
            head = head.next
        arr1 = arr[:len(arr)//2]
        arr2 = arr[len(arr)//2:][::-1]
        dummy = curr = ListNode(0)

        for i in range(len(arr1)):
            curr.next = arr1[i]
            curr.next.next = arr2[i]
            curr = curr.next.next
        if len(arr2) > len(arr1):
            curr.next = arr2[-1]
            curr = curr.next
            
        curr.next = None
