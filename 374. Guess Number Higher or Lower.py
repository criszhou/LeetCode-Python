# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        Min = 1
        Max = n

        while Min<Max:
            guessNum = (Max+Min)//2
            guessRes = guess(guessNum)
            if guessRes==0:
                return guessNum
            elif guessRes==1:
                Min = guessNum + 1
            elif guessRes==-1:
                Max = guessNum - 1

        assert Min==Max
        return Min