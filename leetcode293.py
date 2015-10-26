class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for idx in range(1, len(s)):
            if s[idx] == s[idx-1] == "+":
                res.append(s[:idx-1] + "--" + s[idx+1:])

        return res
                
        