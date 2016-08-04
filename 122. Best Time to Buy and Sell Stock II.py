class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lastPrice = float('inf')

        ret = 0
        for p in prices:
            ret += max(p - lastPrice, 0)
            lastPrice = p

        return ret