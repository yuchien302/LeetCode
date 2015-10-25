from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = deque()

        for i in range(len(nums)):
            if len(q) > 0 and q[0] <= i - k:
                q.popleft()
                
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if i >= k-1:
                res.append(nums[q[0]])
            
        return res
