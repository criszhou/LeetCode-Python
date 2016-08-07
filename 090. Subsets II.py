from collections import Counter


class Solution(object):
    def subsetsWithDupHelper(self, numCountPairs, partialRes, results):
        if not numCountPairs:
            results.append(list(partialRes))
            return

        (num, count) = numCountPairs.pop()

        self.subsetsWithDupHelper(numCountPairs, partialRes, results)
        for i in range(count):
            partialRes.append(num)
            self.subsetsWithDupHelper(numCountPairs, partialRes, results)
        del partialRes[-count:]

        numCountPairs.append((num, count))

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        numCountPairs = [(num, count) for (num, count) in Counter(nums).items()]

        self.subsetsWithDupHelper(numCountPairs, [], ret)

        return ret

