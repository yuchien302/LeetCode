class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return []
        res.append([nums[0], nums[0]])
        for i in range(1, len(nums)):
            if res and nums[i-1] == nums[i] - 1:
                res[-1][1] = nums[i]
            else:
                res.append([nums[i], nums[i]])
        
        return map(lambda r: str(r[0])+"->"+str(r[1]) if r[0]!=r[1] else str(r[0]), res)