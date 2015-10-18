# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
            
        l = 1
        r = n
        m = (l+r)/2
        
        while r > l:
            if not isBadVersion(m) and isBadVersion(m+1):
                return m+1
            elif isBadVersion(m):
                r = m
                m = (l+r)/2
            else:
                l = m
                m = (l+r)/2
        