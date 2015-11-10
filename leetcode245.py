from collections import defaultdict
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dict = defaultdict(list)
        for i, w in enumerate(words):
            dict[w].append(i)
            
        return min([abs(i1-i2) for i1 in dict[word1] for i2 in dict[word2] if i1 != i2])