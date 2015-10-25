class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                sum3 = sum([num, nums[l], nums[r]])
                if abs(target - sum3) < abs(res-target):
                    res = sum3
                if sum3 > target:
                    r -= 1
                elif sum3 < target:
                    l += 1
                else:
                    break
        return res
