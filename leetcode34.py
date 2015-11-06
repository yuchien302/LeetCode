class Solution(object):

                
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums)
        left, right = -1, -1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] < target: lo = mid + 1
            else: hi = mid

        if lo < len(nums) and nums[lo] == target:
            left = lo
            
        lo, hi = left, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if target < nums[mid]: hi = mid
            else: lo = mid + 1

        if 0 < hi and nums[hi-1] == target:
            right = hi-1
            
        return [left, right]