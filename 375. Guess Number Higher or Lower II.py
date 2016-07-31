class Solution(object):
    def getMoneyAmountHelper(self, Min, Max, n, resultCache):
        """
        same as main function, just instead of target in [1,n], now it can be in [Min,Max]
        n is not quite necessary here, it's here to make the cache faster (int key better than tuple key)
        """
        if not Min < Max:
            return 0

        cacheKey = Min * n + Max

        if cacheKey not in resultCache:
            ret = (Min + Max - 1) * (Max - Min) // 2  # upper bound of cost, sum of all numbers in [Min, Max)
            for guess in range((Min + Max) // 2, Max):  # never need to guess Max
                part1Min = self.getMoneyAmountHelper(Min, guess - 1, n, resultCache)
                part2Min = self.getMoneyAmountHelper(guess + 1, Max, n, resultCache)
                ret = min(ret, guess + max(part1Min, part2Min))

                if part1Min >= part2Min:
                    break  # because if we further increase guess, part1Min will increase, part2Min will decrease, so max of the 2 will increase. This round cost (guess) will also increase. So no need to keep going
            resultCache[cacheKey] = ret

        return resultCache[cacheKey]

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        resultCache = dict()
        return self.getMoneyAmountHelper(Min=0, Max=n, n=n, resultCache=resultCache)