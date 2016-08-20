class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0

        ret = len(nums)

        first, last = 0, 0
        windowSum = nums[0]
        while True:
            if windowSum >= s:
                ret = min(ret, last + 1 - first)
                windowSum -= nums[first]
                first += 1
            elif windowSum < s and last + 1 < len(nums):
                last += 1
                windowSum += nums[last]
            else:
                break

        return ret
