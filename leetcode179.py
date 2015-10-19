class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(cmp=lambda a, b: cmp(b+a, a+b))
        return ''.join(nums).lstrip("0") or "0"
        