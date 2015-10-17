class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        idx2, idx3, idx5 = 0, 0, 0
        u = [1]
        for i in range(1, n):
            u.append(min([u[idx2] * 2, u[idx3] * 3, u[idx5] * 5]))
            if u[-1] == u[idx2] * 2:
                idx2 += 1
                
            if u[-1] == u[idx3] * 3:
                idx3 += 1
                
            if u[-1] == u[idx5] * 5:
                idx5 += 1
                
        return u[-1]
