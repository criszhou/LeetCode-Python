class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        currSum = 0

        for n in nums:
            currSum += n

            currSum = max(currSum, 0)
            ret = max(ret, currSum)

        return ret if ret>0 else max(nums)