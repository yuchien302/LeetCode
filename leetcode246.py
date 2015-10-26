from math import ceil
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return all( [num[i] + num[~i] in "00 11 88 696" for i in range(int(len(num)/2) + 1)] )