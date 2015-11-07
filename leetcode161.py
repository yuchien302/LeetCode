class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if abs(len(s) - len(t)) > 1:
            return False
            
        elif len(s) == len(t):
            return len(filter(lambda (c1, c2): c1 != c2, zip(s, t))) == 1

        else:
            if len(s) < len(t):
                s, t = t, s
                
            if s[:-1] == t:
                return True
            
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
                    
        return False