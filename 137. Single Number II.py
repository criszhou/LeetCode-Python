class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = 0
        twice = 0

        for num in nums:
            newTwice = (twice & (~num)) | (once & num)
            newOnce = (once & (~num)) | (num & (~once) & (~twice))
            once, twice = newOnce, newTwice

        return once