class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candidate = 0
        level = 0

        for num in nums:
            if num == candidate:
                level += 1
            elif level==0:
                candidate = num
                level += 1
            else:
                level -= 1

        return candidate