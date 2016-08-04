class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1 for n in nums]

        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i-1]
            ret[i] *= prod

        prod = 1
        for i in range(len(nums)-2,-1,-1):
            prod *= nums[i+1]
            ret[i] *= prod

        return ret