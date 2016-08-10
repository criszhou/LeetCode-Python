class Solution(object):
    def permuteUniqueHelper(self, nums, fixedBefore, results):
        if fixedBefore==len(nums):
            results.append( list(nums) )
            return

        swappedNums = set()
        for i in range(fixedBefore,len(nums)):
            if nums[i] not in swappedNums:
                nums[fixedBefore], nums[i] = nums[i], nums[fixedBefore]
                self.permuteUniqueHelper(nums, fixedBefore+1, results)
                nums[fixedBefore], nums[i] = nums[i], nums[fixedBefore]

                swappedNums.add(nums[i])


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.permuteUniqueHelper(nums, fixedBefore=0, results=ret)
        return ret
