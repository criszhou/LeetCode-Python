class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0

        for i, c in enumerate(s):
            next_char = s[i + 1] if i + 1 < len(s) else '_'

            if c == 'M':
                ret += 1000
            elif c == 'D':
                ret += 500
            elif c == 'C':
                ret += 100 if next_char not in 'MD' else -100
            elif c == 'L':
                ret += 50
            elif c == 'X':
                ret += 10 if next_char not in 'CL' else -10
            elif c == 'V':
                ret += 5
            elif c == 'I':
                ret += 1 if next_char not in 'XV' else -1

        return ret