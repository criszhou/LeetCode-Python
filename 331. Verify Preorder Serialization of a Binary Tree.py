from itertools import chain

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        spaceCount = 1

        prevC = None
        for c in chain( preorder, ',' ):
            if c==',':
                if spaceCount <= 0:
                    return False

                if prevC != '#': # this is a valid node
                    spaceCount += 1
                elif prevC == '#': # this is a None
                    spaceCount -= 1

            prevC = c

        return spaceCount == 0