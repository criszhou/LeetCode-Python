class Solution(object):
    def superPow(self, a, b, mod=1337):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        a = a % mod
        ret = 1

        for ex in b:
            ret = pow(ret, 10, mod)
            ret *= pow(a, ex, mod)
            ret %= mod

        return ret