from bisect import bisect_left

class Solution(object):
    def longestIncreasingSubseqLength(self, nums):
        """
        return the length of longest increasing subsequence
        """
        LISlist = [] # LISlist[i] is the minimal last num of length-(i+1) subsequence
        for num in nums:
            pos = bisect_left( LISlist, num )
            if pos == len(LISlist):
                LISlist.append( num )
            else:
                LISlist[ pos ] = num

        return len(LISlist)

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # we first sort by x, then by y but in reverse order
        # In this way, an increasing subsequence in y values will guarantee increasing in both x and y
        sortedEnvelopes = sorted( envelopes, key=lambda coord: (coord[0],-coord[1]) )

        return self.longestIncreasingSubseqLength( y for x,y in sortedEnvelopes )