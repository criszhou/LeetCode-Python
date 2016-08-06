class Solution(object):
    grayCodeCache = [0,1]

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        while len(self.grayCodeCache) < (1<<n):
            currLen = len(self.grayCodeCache)
            add = self.grayCodeCache[-1] << 1

            for i in range(currLen-1,-1,-1):
                self.grayCodeCache.append( self.grayCodeCache[i] + add )

        return self.grayCodeCache[:(1<<n)]

solver = Solution()
print( solver.grayCode(3) )