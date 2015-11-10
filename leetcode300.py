class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i, num in enumerate(nums):

            dp.append(max([dp[j]+1 for j in range(i) if nums[j] < nums[i]] + [1]))
        return max(dp) if dp else 0
            