import math


class Solution(object):
    getFactorsCache = dict()

    def getFactors(self, n, includeN=False):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n not in self.getFactorsCache:
            ret = [[n]]

            for f in range(2, int(math.sqrt(n)) + 1):
                if n % f == 0:
                    ret.extend(([f] + result) for result in self.getFactors(n//f, includeN=True) if result[0] >= f)

            self.getFactorsCache[n] = ret

        ret = list(self.getFactorsCache[n])
        if not includeN:
            ret.remove([n])

        return ret