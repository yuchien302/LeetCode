from itertools import groupby
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = "1"
        while n > 1:
            strs = [ str(len(list(g[1]))) + g[0] for g in groupby(a)]
            a = ''.join(strs)
            n -= 1
        return a
        