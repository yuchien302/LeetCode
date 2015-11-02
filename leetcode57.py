# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        left = filter(lambda i: i.end < newInterval.start, intervals)
        right = filter(lambda i: newInterval.end < i.start, intervals)


        middle = (set(intervals) - set(left) - set(right)) | set([newInterval])
        start = min([i.start for i in middle])
        end = max([i.end for i in middle])
        
        return left + [Interval(start, end)] + right
                
                
            
        