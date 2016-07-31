class Solution(object):
    countBitsRes = [0]

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        while num >= len(self.countBitsRes):
            currLen = len(self.countBitsRes)
            for i in range(currLen):
                self.countBitsRes.append(1 + self.countBitsRes[i])

        return self.countBitsRes[:num + 1]