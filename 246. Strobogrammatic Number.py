class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        len2strs = { "00", "11", "88", "69", "96" }
        len1strs = { "0", "1", "8" }

        s = str(num)

        while len(s)>2:
            if s[0]+s[-1] not in len2strs:
                return False
            s = s[1:-1]

        return s in len2strs or s in len1strs