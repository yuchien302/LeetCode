from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
            
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            
        return [ key for key, value in count.items() if value > len(nums) // 3]
        # return max(count, key=count.get)