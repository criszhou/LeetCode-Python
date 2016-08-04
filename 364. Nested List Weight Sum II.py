# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
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

class Solution(object):
    def depthSumInverseHelper(self, nestedList, currLevel, levelSums):
        for e in nestedList:
            if e.isInteger():
                while currLevel >= len(levelSums):
                    levelSums.append(0)
                levelSums[currLevel] += e.getInteger()
            else:
                self.depthSumInverseHelper(e.getList(), currLevel+1, levelSums)

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        levelSums = []
        self.depthSumInverseHelper(nestedList, currLevel=0, levelSums=levelSums)

        return sum( (level+1)*Sum for level,Sum in enumerate(reversed(levelSums)) )
