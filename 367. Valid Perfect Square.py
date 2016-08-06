class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False

        sqrtMin = 0
        sqrtMax = num

        while sqrtMin < sqrtMax:
            sqrtMid = (sqrtMin+sqrtMax)//2

            Mid = sqrtMid ** 2
            if num == Mid:
                return True
            elif num < Mid:
                sqrtMax = sqrtMid-1
            else:
                sqrtMin = sqrtMid+1

        return any( num==x**2 for x in range(sqrtMin,sqrtMax+1) )