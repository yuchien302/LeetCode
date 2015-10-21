class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
            
        if len(triangle) == 1:
            return triangle[0][0]
            
        height = len(triangle)
        dp = [2147483647] * height
        dp[0] = triangle[0][0]
        
        
        for h in range(1, height):
            dp_next = dp[:]
            dp_next[0] = triangle[h][0] + dp[0]
            
            for i in range(1, h+1):
                dp_next[i] = triangle[h][i] + min(dp[i-1], dp[i])

            dp = dp_next[:]

        return min(dp)