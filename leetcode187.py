from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dnas = defaultdict(int)
        res = []
        for i in range(10, len(s)+1):
            if dnas[s[i-10:i]] == 1:
                res.append(s[i-10:i])
            dnas[s[i-10:i]] += 1
        return res