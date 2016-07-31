class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        # find how many times does the non-zero diff changes sign

        ret = 1
        diffSign = 0
        lastNum = nums[0]

        for num in nums:
            if num != lastNum:
                newDiffSign = +1 if num>lastNum else -1
                if newDiffSign != diffSign:
                    ret += 1

                diffSign = newDiffSign
                lastNum = num

        return ret