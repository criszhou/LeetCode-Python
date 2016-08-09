class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        assert len(nums)>=3

        if len(nums)==3:
            return sum(nums)

        nums = sorted(nums)
        ret = sum(nums[:3])
        if ret==target:
            return ret

        for i2 in range(1,len(nums)-1):
            i1 = 0
            i3 = len(nums)-1

            while i1<i2<i3:
                currSum = nums[i1] + nums[i2] + nums[i3]

                if currSum==target:
                    return target
                elif abs(currSum-target) < abs(ret-target):
                    ret = currSum

                if currSum < target:
                    i1 += 1
                else:
                    i3 -= 1

        return ret