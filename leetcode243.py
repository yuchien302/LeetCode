class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = -1, -1
        res = len(words)
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            if w == word2:
                i2 =i
            if i1 != -1 and i2 != -1:
                res = min(abs(i1-i2), res)
                
        return res