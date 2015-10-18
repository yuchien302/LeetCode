class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums)-1
        i = 0
        while i <= back:
            if nums[i] == 0:
                nums[i], nums[front] = nums[front], nums[i] 
                front += 1
                
            if nums[i] == 2:
                nums[i], nums[back] = nums[back], nums[i] 
                back -= 1
                i -= 1
            i += 1