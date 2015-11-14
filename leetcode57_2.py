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
        res = []
        inserted = False
        for inter in intervals:
            if inserted or inter.end < newInterval.start:
                res.append(inter)
            elif not inserted and newInterval.end < inter.start:
                res.append(newInterval)
                res.append(inter)
                inserted = True
            else:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end = max(newInterval.end, inter.end)
        if not inserted:
            res.append(newInterval)
        return res
            
        