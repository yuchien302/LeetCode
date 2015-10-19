class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for idx, n in enumerate(nums):
            mem[n] = idx
            
        for idx, n in enumerate(nums):
            if target-n in mem and idx != mem[(target-n)]:
                return sorted([ idx+1, mem[(target-n)]+1 ])
        return []