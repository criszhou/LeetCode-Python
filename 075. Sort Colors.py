class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        writeL, writeR = 0, len(nums) - 1
        read = 0
        pivot = 1

        while read <= writeR:
            if nums[read] == pivot:
                read += 1
            elif nums[read] < pivot:
                nums[read], nums[writeL] = nums[writeL], nums[read]
                read += 1
                writeL += 1
            else:
                nums[read], nums[writeR] = nums[writeR], nums[read]
                writeR -= 1
