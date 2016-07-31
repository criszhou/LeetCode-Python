# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [ [nestedList, 0] ]

    def _moveToValid(self):
        """
        move stack to a valid position, so that the last place is an integer
        """
        while self.stack:
            lastList, lastIdx = self.stack[-1]
            if lastIdx<len(lastList) and lastList[lastIdx].isInteger():
                return
            elif lastIdx == len(lastList):
                self.stack.pop()
                if self.stack:
                    self.stack[-1][1] += 1
            elif lastList[lastIdx].isInteger() == False:
                self.stack.append( [ lastList[lastIdx].getList(), 0 ] )

    def next(self):
        """
        :rtype: int
        """
        self._moveToValid()
        lastList, lastIdx = self.stack[-1]
        ret = lastList[lastIdx].getInteger()
        self.stack[-1][1] += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        self._moveToValid()
        return bool(self.stack)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())