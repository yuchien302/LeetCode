class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums) // 2
        res = []
        for i in range(length):
            res.append(nums[i])
            res.append(nums[i+len(nums)//2])
        if len(nums) % 2 == 1:
            res.append(nums[-1])
            if len(nums) > 1:
                res[-1], res[-2] = res[-2], res[-1]
        nums[:] = res
        