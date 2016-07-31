class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numToIndex = dict() # maps a number in nums to its index

        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return (numToIndex[target - num], i)

            numToIndex[num] = i

        assert False  # this question assumes input would have exactly one solution