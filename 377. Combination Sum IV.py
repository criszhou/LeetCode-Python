class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        resCache = [None] * (target+1) # resCache[k] is the number of ways to add to k
        resCache[0] = 1

        for k in range(1,target+1):
            res = 0

            for num in nums:
                if k-num<0:
                    break
                res += resCache[k-num]

            resCache[k] = res

        return resCache[target]