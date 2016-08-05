class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        ret = 0
        for i in range(len(nums)):
            k = len(nums)-1

            for j in range(i+1,len(nums)):
                while j<k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1

                if k==j:
                    break

                ret += k-j


        return ret