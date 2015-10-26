from itertools import groupby
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(filter(lambda n: n%2==1, map(lambda g: len(list(g[1])),groupby(sorted(s))))) <= 1
        