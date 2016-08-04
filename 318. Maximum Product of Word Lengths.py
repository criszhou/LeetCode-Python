import operator


# from functools import reduce # python 3 only

class Solution(object):
    def wordToBit(self, word):
        if word == "":
            return 0

        return reduce(operator.or_, (1 << (ord(c) - ord('a')) for c in word))

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsInfo = [(len(w), self.wordToBit(w)) for w in words]  # (length, bit) for each word
        ret = 0
        for i in range(len(wordsInfo)):
            for j in range(i, len(wordsInfo)):
                len1, bit1 = wordsInfo[i]
                len2, bit2 = wordsInfo[j]

                if bit1 & bit2 == 0:
                    ret = max(ret, len1 * len2)

        return ret