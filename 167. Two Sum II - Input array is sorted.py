class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i1, i2 = 0, len(numbers)-1

        while i1<i2:
            thisSum = numbers[i1] + numbers[i2]
            if thisSum == target:
                return (i1+1, i2+1)
            elif thisSum > target:
                i2 -= 1
            else:
                i1 += 1

        assert False