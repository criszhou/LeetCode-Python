class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num >= 4:
            if num & 3 == 0:
                num //= 4
            else:
                return False

        return num == 1