class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0

        while n:
            n &= n - 1
            ret += 1

        return ret