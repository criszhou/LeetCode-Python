from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        sqrtN = int(sqrt(n))
        for x in range(sqrtN + 1):
            if isPrime[x]:
                m = x ** 2
                while m < n:
                    isPrime[m] = False
                    m += x

        return sum(1 for isp in isPrime if isp)