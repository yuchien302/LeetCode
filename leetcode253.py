# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        room_count, max_room_count = 0, 0
        available = 0
        s, e = 0, 0
        while s < len(intervals) :
            if end[e] > start[s]:
                if available == 0:
                    room_count += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1


        return room_count
            