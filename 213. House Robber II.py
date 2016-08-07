class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        # first find result of nums[:-1]
        last1 = 0  # last result
        last2 = 0  # the one before last result

        for i in range(len(nums) - 1):
            num = nums[i]
            newLast1 = max(last1, last2 + num)
            last2 = last1
            last1 = newLast1

        ret1 = last1

        # then find result of nums[1:]
        last1 = 0  # last result
        last2 = 0  # the one before last result

        for i in range(1, len(nums)):
            num = nums[i]
            newLast1 = max(last1, last2 + num)
            last2 = last1
            last1 = newLast1

        ret2 = last1

        return max(ret1, ret2)

