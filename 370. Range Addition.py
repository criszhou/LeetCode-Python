class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ret = [0] * (length + 1)

        for (first, last, change) in updates:
            ret[first] += change
            ret[last + 1] -= change

        for i in range(1, length + 1):
            ret[i] += ret[i - 1]

        ret.pop()
        return ret