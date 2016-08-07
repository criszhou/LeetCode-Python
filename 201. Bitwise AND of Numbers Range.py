class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = n
        while ret > m:
            ret &= ret - 1

        return ret