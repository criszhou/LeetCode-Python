from itertools import chain

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s

        retLists = [ [] for i in range(numRows) ]
        currRow = 0
        direction = +1

        for c in s:
            retLists[currRow].append(c)
            currRow += direction

            if currRow in (0, numRows-1):
                direction *= -1

        return "".join( chain.from_iterable( retLists ) )