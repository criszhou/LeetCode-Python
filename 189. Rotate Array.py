class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        k %= len(nums)

        if k==0:
            return

        nums.reverse()

        i1,i2 = 0,k-1
        while i1<i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1+=1
            i2-=1

        i1,i2 = k,len(nums)-1
        while i1<i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1+=1
            i2-=1