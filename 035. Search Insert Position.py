class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # import bisect
        # return bisect.bisect_left( nums, target )
        if not nums or target<nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        Min = 0
        Max = len(nums)-1

        while Max - Min > 3:
            Mid = (Max+Min)//2
            if nums[Mid] == target:
                return Mid
            elif nums[Mid] > target:
                Max = Mid
            elif nums[Mid] < target:
                Min = Mid+1

        for ret in range(Min,Max+1):
            if target <= nums[ret]:
                return ret
        else:
            return Max+1