class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = num%9

        if ret==0 and num>0:
            ret = 9

        return ret