class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        oddChars = set()

        for c in s:
            if c in oddChars:
                oddChars.remove(c)
            else:
                oddChars.add(c)

        return len(oddChars) <= 1