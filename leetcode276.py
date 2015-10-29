class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums_s = [0] * (n+1) # single
        nums_r = [0] * (n+1) # repeat
        if n == 0:
            return 0
            
        nums_s[1] = k
        nums_r[1] = 0

        for i in range(2, n+1):
            nums_s[i] = nums_s[i-1] * (k-1) + nums_r[i-1] * (k-1)
            nums_r[i] = nums_s[i-1]
            
        return nums_s[n] + nums_r[n]