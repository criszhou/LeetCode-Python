class Solution(object):
    def permuteHelper(self, nums, fixedBefore, results):
        if fixedBefore >= len(nums):
            results.append( list(nums) )
            return

        for toSwap in range(fixedBefore, len(nums)):
            nums[fixedBefore], nums[toSwap] = nums[toSwap], nums[fixedBefore]
            self.permuteHelper(nums, fixedBefore+1, results)
            nums[fixedBefore], nums[toSwap] = nums[toSwap], nums[fixedBefore]

    def permute(self, nums, fixedBefore=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.permuteHelper(nums, 0, ret)
        return ret