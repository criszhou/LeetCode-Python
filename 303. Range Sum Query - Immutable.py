class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.partialSums = [0] + nums

        for i in range(1,len(self.partialSums)):
            self.partialSums[i] += self.partialSums[i-1]

        # self.partialSums[k] == nums[:k]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.partialSums[j+1] - self.partialSums[i]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)