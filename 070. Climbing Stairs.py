class Solution(object):
    climbStairsResults = [1,1]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n >= len(self.climbStairsResults):
            self.climbStairsResults.append( self.climbStairsResults[-1] + self.climbStairsResults[-2] )

        return self.climbStairsResults[n]
