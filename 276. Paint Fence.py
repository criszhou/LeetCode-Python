class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int, number of posts
        :type k: int, number of colors
        :rtype: int
        """
        if n==0 or k==0:
            return 0

        lastSame = 0 # number of ways where last 2 posts have same color
        lastDiff = k # number of ways where last 2 posts have different colors

        for m in range(n-1):
            newLastSame = lastDiff
            newLastDiff = ( lastSame + lastDiff ) * ( k - 1 )
            lastSame, lastDiff = newLastSame, newLastDiff

        return lastSame + lastDiff