class Solution(object):
    def coinChangeHelper(self, coins, amount, resCache):
        # coins should be strictly decreasing

        # use memoization
        if amount not in resCache:
            ret = float('inf')

            for coin in coins:
                if coin > amount:
                    continue

                if amount // coin >= ret: # short cut, no need to continue because we may as well use large coin first
                    break

                ret = min(ret, 1 + self.coinChangeHelper(coins, amount - coin, resCache))

            resCache[amount] = ret

        return resCache[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort( key = lambda x: -x )
        resCache = {c: 1 for c in coins}
        resCache[0] = 0

        for rem in range(amount % coins[0], amount, coins[0]):
            self.coinChangeHelper(coins, amount, resCache)  # this step is to shorten the stack depth in next step

        ret = self.coinChangeHelper(coins, amount, resCache)
        if ret == float('inf'):
            ret = -1

        return ret
