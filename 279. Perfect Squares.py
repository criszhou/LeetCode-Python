from math import sqrt

class Solution(object):
    resultCache = [0, 1, 2, 3]  # resultCache[n]==k means n can be represented as sum of k squares

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        while len(self.resultCache) <= n:
            m = len(self.resultCache)
            sqrtm = int(sqrt(m))

            if m == sqrtm**2:
                ret = 1
            else:
                ret = 4 # Lagrange's four-square theorem. Can replace 4 with m, will still work, just slower
                qLB = int( sqrt( m // (ret-1) ) ) # lower bound of q to make ret smaller

                for q in range(sqrtm, 0, -1):
                    if 1 + self.resultCache[m-q**2] < ret:
                        ret = 1 + self.resultCache[m-q**2]
                        qLB = int(sqrt(m // (ret-1)))

                    if q < qLB:
                        break

            self.resultCache.append(ret)

        return self.resultCache[n]