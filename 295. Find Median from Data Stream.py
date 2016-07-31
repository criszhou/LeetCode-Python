from heapq import heappush, heappop, heappushpop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')]
        # lowerHeap's numbers are minus original numbers, because in Python heap is min-heap

        # always maintain that their lens are equal, or upper has 1 more than lower

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]

        if num > upperMin or (lowerMax<=num<=upperMin and len(self.upperHeap)==len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)

        # maintain the invariant that their lens are equal, or upper has 1 more than lower
        if len(self.upperHeap)-len(self.lowerHeap) > 1:
            heappush( self.lowerHeap, -heappop( self.upperHeap ) )
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush( self.upperHeap, -heappop( self.lowerHeap ) )


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.upperHeap) == len(self.lowerHeap):
            upperMin = + self.upperHeap[0]
            lowerMax = - self.lowerHeap[0]
            return ( float(upperMin) + float(lowerMax) ) / 2.0
        else:
            assert len(self.upperHeap) == len(self.lowerHeap) + 1
            return float(self.upperHeap[0])


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()