import operator

class Solution(object):
    resCache = dict() # key is an expression, value is the list of calculated results
    charToOperator = { "+":operator.add, "-":operator.sub, "*":operator.mul }

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input not in self.resCache:
            ret = []

            hasOperator = False
            for i,c in enumerate(input):
                if c in "+-*":
                    hasOperator = True

                    leftResults  = self.diffWaysToCompute( input[:i]   )
                    rightResults = self.diffWaysToCompute( input[i+1:] )
                    op = self.charToOperator[c]

                    ret.extend( op( resL, resR ) for resL in leftResults for resR in rightResults )

            if not hasOperator:
                ret.append( int(input) )

            self.resCache[ input ] = ret

        return self.resCache[ input ]