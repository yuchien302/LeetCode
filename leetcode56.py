# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return []
        res = []
        res.append(intervals[0])
        for interval in intervals[1:]:
            if res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(interval.end, res[-1].end)
        return res
            
        