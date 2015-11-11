class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        elif needle == "":
            return 0
        
        n = len(needle)
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+n] == needle:
                return i
                
        return -1
        