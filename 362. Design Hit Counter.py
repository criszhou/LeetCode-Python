from collections import deque

class HitCounter(object):
    windowLen = 300

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitQueue = deque() # each item is a pair [timeStamp,hitCount] where hitCount is the number of hits at timeStamp
        self.hitCountInWindow = 0

    def _removeOldHits(self, timestamp):
        while self.hitQueue and self.hitQueue[0][0] <= timestamp - self.windowLen:
            self.hitCountInWindow -= self.hitQueue.popleft()[1]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not ( self.hitQueue and self.hitQueue[-1][0]==timestamp ):
            self.hitQueue.append( [timestamp,0] )

        self.hitQueue[-1][1] += 1
        self.hitCountInWindow += 1

        # self._removeOldHits(timestamp) # seems removing line this makes it faster

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self._removeOldHits(timestamp)
        return self.hitCountInWindow



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)