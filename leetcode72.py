class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row = len(word1)
        col = len(word2)
        if row == 0:
            return col
        elif col == 0:
            return row
            
        dp = [[ 0 for _ in range(col+1) ] for _ in range(row+1)]
        
        for c in range(col+1):
            dp[0][c] = c
            
        for r in range(row+1):
            dp[r][0] = r
        
        for r in range(1, row+1):
            for c in range(1, col+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min( dp[r-1][c], dp[r][c-1], dp[r-1][c-1] ) + 1
                    
        return dp[row][col]
                
                
                
        