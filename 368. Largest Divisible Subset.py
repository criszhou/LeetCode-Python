class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = sorted(nums)

        if len(nums) <= 1:
            return nums

        prevNumIds = []  # prevNumIds[i]==j means j<i and nums[i]%nums[j]==0 and j is the best to form largest divisible subset
        divSubsetLens = []  # divSubsetLens[i]==k the largest divisible subset ending at nums[i] has length k

        largestDivSubsetEndIndex = 0

        for i, num in enumerate(nums):
            prevNumId = None
            divSubsetLen = 1

            for j in range(i):
                if nums[i] % nums[j] == 0 and divSubsetLens[j] + 1 > divSubsetLen:
                    prevNumId = j
                    divSubsetLen = divSubsetLens[j] + 1

            prevNumIds.append(prevNumId)
            divSubsetLens.append(divSubsetLen)

            if divSubsetLen > divSubsetLens[largestDivSubsetEndIndex]:
                largestDivSubsetEndIndex = i

        retIds = [largestDivSubsetEndIndex]
        while prevNumIds[retIds[-1]] != None:
            retIds.append(prevNumIds[retIds[-1]])

        return [nums[i] for i in reversed(retIds)]