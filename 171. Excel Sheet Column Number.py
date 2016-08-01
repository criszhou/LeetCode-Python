class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum( ( ord(c) - ord('A') + 1 ) * (26**i) for i,c in enumerate(reversed(s)) )
