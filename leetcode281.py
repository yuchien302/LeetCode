class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.res = []
        n = min( len(v1), len(v2) )
        for i in range(n):
            self.res.append(v1[i])
            self.res.append(v2[i])
        if n == len(v1):
            self.res.extend(v2[len(v1):])
        else:
            self.res.extend(v1[len(v2):])
            
        self.idx = 0
            
            

    def next(self):
        """
        :rtype: int
        """
        val = self.res[self.idx]
        self.idx += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.res)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())