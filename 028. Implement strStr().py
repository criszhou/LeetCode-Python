class Solution(object):
    @staticmethod
    def KMP_failure_table(pattern):
        """
        :param pattern: str
        :return: the failure table for KMP algorithm
        ret[i] should be the maximal j s.t. pattern[:j] is a suffix of pattern[:i+1], and j<i+1
        """
        # ret = []
        # for i,c in enumerate(pattern):
        #     ret.append( max( [ k for k in range(i+1) if pattern[:i+1].endswith( pattern[:k] ) ] + [ 0 ] ) )
        ret = []

        for i, c in enumerate(pattern):
            if i == 0:
                ret.append(0)
            else:
                j = ret[-1]
                while j > 0 and c != pattern[j]:
                    j = ret[j-1]

                if c == pattern[j]:
                    j += 1

                ret.append(j)

        return ret

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif len(needle) > len(haystack):
            return -1
        elif len(needle) == len(haystack):
            return 0 if needle == haystack else -1

        failureTable = self.KMP_failure_table(needle)

        # j is the needle index, i is the haystack index
        j = 0
        for i, c in enumerate(haystack):
            while j > 0 and haystack[i] != needle[j]:
                j = failureTable[j - 1]

            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1

        return -1