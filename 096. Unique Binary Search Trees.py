class Solution(object):
    resCache = [1,1,2]
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n >= len(self.resCache):
            m = len(self.resCache)

            mRet = 0
            for leftTreeSize in range(0,m):
                rightTreeSize = m-1-leftTreeSize
                mRet += self.resCache[leftTreeSize] * self.resCache[rightTreeSize]

            self.resCache.append(mRet)

        return self.resCache[n]