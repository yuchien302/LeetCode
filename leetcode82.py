# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = dummy.next
        del_value = None
        
        while curr:
            if curr.val == del_value:
                prev.next = curr.next
                curr = curr.next
                continue
            
            if curr.next and curr.val == curr.next.val:
                del_value = curr.val
                continue
            
            prev = curr    
            curr = curr.next
            

        return dummy.next
                
            