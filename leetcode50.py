class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = abs(n)
            x = 1.0 / x
            
        if x == 0:
            return 0
            
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return self.myPow(x * x, n//2) * self.myPow(x, n % 2)
        