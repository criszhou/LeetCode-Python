class Solution(object):
    threePower = 3

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while Solution.threePower < n:
            Solution.threePower *= 3

        return n > 0 and Solution.threePower % n == 0