class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        retList = []
        while n>0:
            n,rem = divmod( n-1, 26 )
            retList.append( chr( ord('A') + rem ) )

        return "".join( reversed( retList ) )