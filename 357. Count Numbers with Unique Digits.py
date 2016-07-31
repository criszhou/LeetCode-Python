class Solution(object):
    def __init__(self):
        self.uniqDigitCount = [1] + list(range(10,0,-1)) # [1,10,9,8,7,6,5,4,3,2,1]

        for i in range(1,len(self.uniqDigitCount)):
            self.uniqDigitCount[i] *= self.uniqDigitCount[i-1]
        # at this point, the i-th number is number of uniq-digit-numbers of length i, may start with 0

        for i in range(1,len(self.uniqDigitCount)):
            self.uniqDigitCount[i] = self.uniqDigitCount[i] // 10 * 9
        # at this point, the i-th number is number of uniq-digit-numbers of length i, may NOT start with 0

        for i in range(1,len(self.uniqDigitCount)):
            self.uniqDigitCount[i] += self.uniqDigitCount[i-1]
        # at this point, the i-th number is number of uniq-digit-numbers of length <=i, may NOT start with 0

        # print(self.uniqDigitCount)

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10: # cannot have say 11 digits all different
            n = 10

        return self.uniqDigitCount[n]