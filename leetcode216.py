class Solution(object):
    
    def helper(self, k, candidates, target):

        res = []
        if len(candidates) == 0:
            return []
        elif candidates[0] > target:
            return []
        elif candidates[0] == target:
            if k == 1:
                return [[target]]
            else:
                return []
        elif target > candidates[0]:
            res.extend([ [candidates[0]] + com for com in self.helper(k-1, candidates[1:], target - candidates[0]) ])

        res.extend(self.helper(k, candidates[1:], target))        
        
        return res             
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(k, range(1, 10), n)
   