class Solution(object):
    def subsetsHelper(self, nums, partialRes, results):
        if not nums:
            results.append( list(reversed(partialRes)) )
            return

        # current number to deside
        num = nums.pop()

        # don't include num
        self.subsetsHelper( nums, partialRes, results )

        # include num
        partialRes.append( num )
        self.subsetsHelper( nums, partialRes, results )
        partialRes.pop()

        # recover
        nums.append( num )


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.subsetsHelper(nums, partialRes=[], results=ret)
        return ret