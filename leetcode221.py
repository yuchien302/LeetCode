class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        if len(matrix[0]) == 1:
            return int(max(map(max, matrix)))
            
            
        dp = [[0 for _ in range(len(matrix[0])+1) ] for _ in range(len(matrix))]
        for i, v in enumerate(matrix[0]):
            dp[0][i+1] = 1 if v == '1' else 0
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])+1):
                a = min(dp[r-1][c], dp[r][c-1])
                if matrix[r][c-1] == '1' and matrix[r-a][c-a-1] == '1':
                    dp[r][c] = a + 1
                elif matrix[r][c-1] == '1':
                    dp[r][c] = max(min(dp[r-1][c], dp[r][c-1]), 1)
            # print(dp)
               
                    
        return max(map(max, dp)) ** 2