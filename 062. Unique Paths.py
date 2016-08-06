class Solution(object):
    NchooseKcache = dict()
    def NchooseK(self, n, k):
        if not 0<=k<=n:
            return 0
        if k==0 or k==n:
            return 1

        cacheKey = (n,k)
        if cacheKey not in self.NchooseKcache:
            self.NchooseKcache[cacheKey] = self.NchooseK(n-1,k) + self.NchooseK(n-1,k-1)
        return self.NchooseKcache[cacheKey]


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m-=1
        n-=1
        return self.NchooseK(m+n,m)