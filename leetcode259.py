class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1    
            while left < right:
                n = nums[i] + nums[left] + nums[right]
                if n < target:
                    count += (right-left)
                    left += 1
                    
                elif n >= target:
                    right -= 1

                    
        return count
                
        