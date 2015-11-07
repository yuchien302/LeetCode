class Solution(object):
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates = sorted([c for c in candidates if c <= target])
        
        res = []
        if len(candidates) == 0:
            return []
        elif candidates[0] > target:
            return []
        elif candidates[0] == target:
            return [[target]]
        elif target > candidates[0]:
            res.extend([ [candidates[0]] + com for com in self.combinationSum(candidates, target - candidates[0]) ])

        res.extend(self.combinationSum(candidates[1:], target))        
        
        return res
        