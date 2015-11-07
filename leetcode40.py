class Solution(object):
    def helper(self, candidates, target):

        
        
        res = []
        if len(candidates) == 0:
            return []
        elif candidates[0] > target:
            return []
        elif candidates[0] == target:
            return [[target]]
        elif target > candidates[0]:
            res.extend([ [candidates[0]] + com for com in self.helper(candidates[1:], target - candidates[0]) ])

        res.extend(self.helper(candidates[1:], target))        

        return res
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted([c for c in candidates if c <= target])
        res = self.helper(candidates, target)
        res = [ list(s) for s in set([tuple(r) for r in res])]
        return res
                