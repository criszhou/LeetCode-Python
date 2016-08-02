class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [1]

        for m in range(rowIndex):
            newNums = [1]
            for i in range(1,len(nums)):
                newNums.append(nums[i]+nums[i-1])
            newNums.append(1)

            nums = newNums

        return nums