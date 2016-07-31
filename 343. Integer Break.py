class Solution(object):
    smallNumRes = [0, 1, 1, 2, 4, 6, 9, 12, 18]
    #              0  1  2  3  4  5  6   7   8

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(self.smallNumRes):
            return self.smallNumRes[n]

        numberOf3 = (n - 5) // 3

        return (3 ** numberOf3) * self.smallNumRes[ n - 3 * numberOf3 ]