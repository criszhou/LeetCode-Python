class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = float("inf") # min so far
        min2 = float("inf") # min of nums[j] s.t. i<j and nums[i]<nums[j]

        for num in nums:
            if min2 < num:
                return True
            elif min1 < num < min2:
                min2 = num
            elif num < min1:
                min1 = num

        return False