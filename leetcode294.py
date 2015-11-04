from collections import deque
class Solution(object):
    
    def flip(self, s):
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1] == "+":
                res.append( s[:i-1] + "--" + s[i+1:] )
        return res
    
    
    def canWinHelper(self, s, m):
        """
        :type s: str
        :rtype: bool
        """
        if s in m:
            return m[s]
            
        flips = self.flip(s)

        if len(flips) == 0:
            m[s] = False
            return False
        
        next_flips = map(self.flip, flips)
        
        for next_flip in next_flips:
            win = True    
            for flip in next_flip:
                win &= self.canWinHelper(flip, m)
            if win:
                m[s] = True
                return True
            
        m[s] = False
        return False
        
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {}
        return self.canWinHelper(s, m)
