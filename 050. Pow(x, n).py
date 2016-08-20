class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0

        if n==0:
            return 1

        if n<0:
            x = 1.0 / x
            n = -n

        if n==1:
            return x

        if n%2==1:
            return x * self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, n//2)