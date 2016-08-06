# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappush, heappop


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        SI = sorted(intervals, key=lambda it: (it.start, it.end))  # sorted intervals

        ret = 0
        heap = []  # contains end times

        for it in SI:
            start, end = it.start, it.end

            while heap and heap[0] <= start:
                heappop(heap)

            heappush(heap, end)

            ret = max(ret, len(heap))

        return ret