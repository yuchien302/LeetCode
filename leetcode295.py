from heapq import * 
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_heap) > len(self.max_heap):
            return 1.0 * self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

            

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()