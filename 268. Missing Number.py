class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expectedSum = len(nums) * (len(nums) + 1) // 2

        return expectedSum - sum(nums)