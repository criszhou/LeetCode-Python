class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        partialSum = 0
        partialSumIndex = {0:0} # maps a partial sum to the first index of it, so maps x to i means nums[:i]==x
        ret = 0

        for i,num in enumerate(nums):
            partialSum += num

            if partialSum-k in partialSumIndex:
                ret = max( ret, i+1 - partialSumIndex[partialSum-k] )

            if partialSum not in partialSumIndex:
                partialSumIndex[partialSum] = i+1

        return ret