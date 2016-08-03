# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        Min = 1
        Max = n

        while Min<Max:
            Mid = (Max+Min)//2
            if isBadVersion( Mid ):
                Max = Mid
            else:
                Min = Mid + 1

        return Min