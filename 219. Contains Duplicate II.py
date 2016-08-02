class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numToIndex = dict()

        for i,num in enumerate(nums):
            if num in numToIndex and i-numToIndex[num]<=k:
                return True
            numToIndex[num] = i

        return False