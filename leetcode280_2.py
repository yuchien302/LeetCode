class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums1 = nums[:len(nums) // 2]
        nums2 = list(reversed(nums[len(nums) // 2:]))
        res = nums[:]
        for i in range(len(nums) // 2):
            res[2*i] = nums1[i]
            res[2*i + 1] = nums2[i]
            
        if len(nums2) != len(nums1):
            res[-1] = nums2[-1]
        nums[:] = res
        