class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0

        while n:
            n //= 5
            ret += n

        return ret