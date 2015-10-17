class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        mem = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for c in range(len(s)+1):
            mem[0][c] = 1
        
        for r in range(1, len(t)+1):
            for c in range(1, len(s)+1):
            
                mem[r][c] = mem[r][c-1] if s[c-1] != t[r-1] else mem[r][c-1] + mem[r-1][c-1]
                
        return mem[len(t)][len(s)]
        