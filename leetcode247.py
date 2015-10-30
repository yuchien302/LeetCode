class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ['0', '1', '8']
        
        if n%2 == 1:
            res = ['0', '1', '8']
        else:
            res = ['']
            
        pos = ['00', '11', '88', '69', '96']
        for _ in range(n // 2):
            res = [ p[0] + r + p[1] for r in res for p in pos]
        
        res = filter(lambda s: s[0] != '0', res)
        return res
        