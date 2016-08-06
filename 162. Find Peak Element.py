class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or nums[0]>=nums[1]:
            return 0

        Min = 1
        Max = len(nums)-1

        while Min < Max:
            Mid = (Min+Max)//2

            if nums[Mid] >= max(nums[Mid-1], nums[Mid+1]):
                return Mid
            elif nums[Mid-1] > nums[Mid]:
                Max = Mid-1
            elif nums[Mid+1] > nums[Mid]:
                Min = Mid+1
            else:
                assert False

        assert Min == Max
        return Min