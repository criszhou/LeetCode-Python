class Solution(object):
    combineCache = dict()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]

        if k == n:
            return [list(range(1, n + 1))]

        cacheKey = (n, k)
        if cacheKey not in self.combineCache:
            self.combineCache[cacheKey] = [(pr + [n]) for pr in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
        return self.combineCache[cacheKey]