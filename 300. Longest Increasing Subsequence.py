import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lisSeq = []  # lisSeq[k] is the minimum last number of increasing subsequence of length k+1

        for num in nums:
            insert = bisect.bisect_left( lisSeq, num )

            if insert == len(lisSeq):
                lisSeq.append( num )
            else:
                lisSeq[ insert ] = num

        return len(lisSeq)