class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < (i+1):
                return i
                
        return len(citations)
                