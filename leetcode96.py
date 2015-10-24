class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [1] * (n+1)
        for i in range(2, n+1):
            count[i] = sum(map(lambda x, y: x*y, count[:i], reversed(count[:i])))
            
        return count[n]
        