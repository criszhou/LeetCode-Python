class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last1 = 0 # last result
        last2 = 0 # the one before last result

        for num in nums:
            newLast1 = max( last1, last2 + num )
            last2 = last1
            last1 = newLast1

        return last1