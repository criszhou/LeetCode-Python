class Solution(object):
    def generateParenthesisHelper(self, n, countL, countR, partialRes, results):
        if countL==countR==n:
            results.append( "".join( partialRes ) )
            return

        canAddLeft  = (countL < n)
        canAddRight = (countR < countL)

        if canAddLeft:
            partialRes.append( '(' )
            self.generateParenthesisHelper(n, countL=countL+1, countR=countR, partialRes=partialRes, results=results)
            partialRes.pop()

        if canAddRight:
            partialRes.append( ')' )
            self.generateParenthesisHelper(n, countL=countL, countR=countR+1, partialRes=partialRes, results=results)
            partialRes.pop()



    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.generateParenthesisHelper(n, countL=0, countR=0, partialRes=[], results=ret)
        return ret