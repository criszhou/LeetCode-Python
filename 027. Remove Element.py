class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1

        return write