class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp_dup, dp_sig = [0]*n, [0]*n
        dp_sig[0] = k
        for i in range(1, n):
            dp_dup[i] = dp_sig[i-1]
            dp_sig[i] = (k-1) * (dp_dup[i-1] + dp_sig[i-1])
            
        return dp_dup[-1] + dp_sig[-1]
            