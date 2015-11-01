class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(len(s)):
            if s[:~i] == (s[:~i])[::-1]:
                return (s[~i:])[::-1] + s

        return ""
        
    # def shortestPalindrome(self, s):
    #     r = s[::-1]
    #     for i in range(len(s) + 1):
    #         if s.startswith(r[i:]):
    #             return(r[:i] + s)