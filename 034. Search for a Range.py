import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(nums, target, lo=left + 1)
        return [left, right - 1]