class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return all([ p[0]+p[1] in "696 88 11 00" for p in zip(num, num[::-1])[:len(num)//2+1]]) 
        