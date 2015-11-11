from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
        
        return [d[0] for d in dict.items() if d[1] == 1][0]