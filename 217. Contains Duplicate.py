class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)

        return False