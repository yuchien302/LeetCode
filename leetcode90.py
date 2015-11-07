class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        l = 0
        for i, n in enumerate(nums):
            if not (i > 0 and nums[i] == nums[i-1]):
                l = len(res)
            res.extend([r + [n] for r in res[len(res)-l : ]])
        return res