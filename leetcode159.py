class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)

        maxlen = 0
        for i in range(2, len(s)):
            c0, c1 = s[i-2], s[i-1]
            idx = i
            if c0 == c1 and s[idx] != c1:
                c1 = s[idx]                
                
            while idx < len(s) and (s[idx] == c0 or s[idx] == c1):
                idx += 1
                if idx < len(s) and c0 == c1 and s[idx] != c1:
                    c1 = s[idx]
            maxlen = max(maxlen, (idx - i)+2)
            
        return maxlen
                