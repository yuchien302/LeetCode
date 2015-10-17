class Solution(object):
    def sub_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        
        t = nums[0]
        n = 0
        
        for i in range(1, len(nums)):
            (t, n) = (n + nums[i], max(t, n))

        return max(t, n)
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
            
        return max(self.sub_rob(nums[1:]), self.sub_rob(nums[:-1]))

        