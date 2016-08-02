from math import log10
from math import floor

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0: return False
        if x < 10: return True

        ten_power = 10 ** int(floor(log10(x)))
        while ten_power > 1:
            if x // ten_power != x % 10: return False
            x = (x % ten_power) // 10
            ten_power = ten_power // 100

        return True