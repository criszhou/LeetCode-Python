class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        nonSpace = None # index of first non-space char of s[::-1]

        for i,c in enumerate(reversed(s)):
            if nonSpace is None and c!=' ':
                nonSpace = i
            elif nonSpace is not None and c==' ':
                return i-nonSpace

        if nonSpace is None:
            return 0
        else:
            return len(s)-nonSpace