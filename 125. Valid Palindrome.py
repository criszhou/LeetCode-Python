class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        i1 = 0
        i2 = len(s)-1

        while i1<i2:
            if not s[i1].isalnum():
                i1 += 1
            elif not s[i2].isalnum():
                i2 -= 1
            elif s[i1].lower() == s[i2].lower():
                i1 += 1
                i2 -= 1
            else:
                return False

        return True