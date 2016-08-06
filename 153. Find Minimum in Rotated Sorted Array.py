class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min, Max = 0, len(nums)-1 # the min and max index of minimum num

        while Max-Min>2:
            if nums[Min] < nums[Max]:
                return nums[Min]

            Mid = (Max+Min)//2
            if nums[Max] < nums[Min] < nums[Mid]:
                Min = Mid + 1
            elif nums[Mid] < nums[Max] < nums[Min]:
                Max = Mid
            else:
                raise Exception()

        return min(nums[Min:Max+1])