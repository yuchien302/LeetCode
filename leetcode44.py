class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = re.sub("\*+", "*", p)
        
        if s == "":
            if p == "" or p == "*":
                return True
            else:
                return False
        elif p == "":
            return False
        
        if len(p.replace("*", "")) > len(s):
            return False
        
        
        dp = [[False for _ in range(len(s))] for _ in range(len(p))]
        
        used = False
        if p[0] in "*?"+s[0]:
            dp[0][0] = True
            if p[0] != "*":
                used = True
            else:
                for c in range(1, len(s)):
                    dp[0][c] = True
        else:
            return False
                
        
        for r in range(1, len(p)):
            
            if used and p[r] != "*":
                break
            
            if p[r] not in "*?" and p[r] != s[0]:
                break
            
            if p[r] == "*":
                dp[r][0] = True

            if not used and p[r] in ("?" + s[0]):
                dp[r][0] = True
                used = True
            
        for c in range(1, len(s)):
            for r in range(1, len(p)):

                if dp[r-1][c-1] and p[r] in ("*?" + s[c]):
                    dp[r][c] = True
                    
                elif dp[r-1][c] and p[r] == "*":
                    dp[r][c] = True
                    
                elif dp[r][c-1] and p[r] == "*":
                    dp[r][c] = True
                    

        return dp[-1][-1]