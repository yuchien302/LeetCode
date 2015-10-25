class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = small = big = nums[0]
        for n in nums[1:]:
            small, big = min(small * n, big * n, n), max(small * n, big * n, n)
            maximum = max(maximum, big)
            
        return maximum
            
            