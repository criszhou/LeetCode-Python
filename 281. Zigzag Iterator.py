class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        if len(v1)==0:
            v1, v2 = v2, v1

        self.currVec = v1
        self.nextVec = v2
        self.currIdx = 0
        self.nextIdx = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.currVec[ self.currIdx ]
        self.currIdx += 1

        if self.nextIdx < len(self.nextVec):
            self.currVec, self.nextVec = self.nextVec, self.currVec
            self.currIdx, self.nextIdx = self.nextIdx, self.currIdx

        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currIdx < len(self.currVec)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())