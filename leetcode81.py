class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
            
        l, r = 0, len(nums)-1
        
        m = int((l+r)/2)
        if nums[m] == target:
            return True
        
        if nums[l] < nums[m]:
            if nums[l] <= target < nums[m]:
                return self.search(nums[l:m], target)
            else:
                return self.search(nums[m+1:r+1], target)
        elif nums[l] > nums[m]:
            if nums[m] < target <= nums[r]:
                return self.search(nums[m+1:r+1], target)
            else:
                return self.search(nums[l:m], target)
        else:
            return self.search(nums[l+1:r+1], target)
        
        