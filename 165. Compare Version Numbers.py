# python 2 use izip_longest
# python 3 use zip_longest
from itertools import izip_longest


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        def versionIter(version):
            begin = 0
            for i, c in enumerate(version):
                if c == '.':
                    yield int(version[begin:i])
                    begin = i + 1
            yield int(version[begin:])

        iter1 = versionIter(version1)
        iter2 = versionIter(version2)
        for g1, g2 in izip_longest(iter1, iter2, fillvalue=0):
            if g1 < g2:
                return -1
            elif g2 < g1:
                return +1

        return 0