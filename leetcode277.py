class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) < 2:
            return True
        root = preorder.pop(0)
        idx = 0
        while idx < len(preorder):
            if preorder[idx] > root:
                break
            idx += 1
        
        mid = idx
        
        while idx < len(preorder):
            if preorder[idx] < root:
                return False
            idx += 1
        
        return self.verifyPreorder(preorder[:mid]) and self.verifyPreorder(preorder[mid:])
        