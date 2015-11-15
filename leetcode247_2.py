class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [""]
        if n%2 == 1:
            res = ["0", "1", "8"]
        strob = ["11", "69", "96", "88", "00"]
        for i in range(n // 2):
            res = [ s[0] + r + s[1] for r in res for s in strob]
            
        return [r for r in res if not (len(r) > 1 and r[0] == '0')]