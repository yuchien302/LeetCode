from guppy import hpy
h = hpy()
class Solution(object):
    def getFactorsGTM(self, n, m):

        res = []
        
        if n >= m:
            res.append([n])
        
        for i in xrange(m, n//2+1):
            
            if n % i == 0:
                res.extend([ [i] + r for r in self.getFactorsGTM(n // i, i)])

        return res        
        
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        h.iso(self.getFactorsGTM(n, 2)[1:]).sp
        return self.getFactorsGTM(n, 2)[1:]



s = Solution()

print(s.getFactors(23848713))
print(h.heap())