class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        for idx, num in enumerate(nums):
            if max_pos < idx:
                return False
                
            max_pos = max(idx + num, max_pos)

        return True
        
        