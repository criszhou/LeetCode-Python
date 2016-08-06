class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0

        for read in range(len(nums)):
            if write>=2 and nums[read]==nums[write-1]==nums[write-2]:
                continue
            else:
                nums[write] = nums[read]
                write += 1

        return write