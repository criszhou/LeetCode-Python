class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastNum = None
        write = 0

        for i in range(len(nums)):
            if nums[i] != lastNum:
                nums[write] = nums[i]
                lastNum = nums[i]
                write += 1

        return write