class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lo, hi = 0, len(citations)
        n = len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if (n - mid) <= citations[mid]:
                hi = mid
            else:
                lo = mid + 1

        return n - hi