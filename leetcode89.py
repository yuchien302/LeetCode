class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        g = [0]
        for i in range(1, n+1):
            for j in range( 2**(i-1)-1, -1, -1):
                g.append( (1<<(i-1)) | g[j])
        return g