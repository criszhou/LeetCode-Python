class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ret = 0

        charToLastIndex = dict()
        currWindowBegin = 0  # starting at this index, we don't have any repeated char

        for i, c in enumerate(s):

            if c in charToLastIndex and charToLastIndex[c] >= currWindowBegin:
                currWindowBegin = charToLastIndex[c] + 1

            ret = max(ret, i + 1 - currWindowBegin)

            charToLastIndex[c] = i

        return ret