class Solution(object):
    def middle(self, fromNum, toNum):
        """
        return the number in the middle of fromNum and toNum
        if there is no such number, return None
        """
        x1,y1 = divmod(fromNum-1, 3)
        x2,y2 = divmod(toNum-1, 3)
        if (x1+x2)%2==0 and (y1+y2)%2==0:
            xm = (x1+x2)//2
            ym = (y1+y2)//2
            return xm*3 + ym + 1
        else:
            return None

    def __init__(self):
        numToPattern = [ 0 ] * 10
        numToPattern[0] = 1
        numToPattern[1] = 9
        # numToPattern[m] is the number of ways to have exactly m numbers

        patternCounts = dict() # key is a pair (remNums,lastNum), remNums is the frozen set of all remaining numbers
                               # value is the number of ways in this pattern

        fullSet = frozenset( i for i in range(1,10) )
        currLevel = { ( fullSet-{i}, i ) for i in range(1,10) }
        for pat in currLevel:
            patternCounts[pat] = 1

        for nextLevelPatternLen in range(2,10):
            nextLevel = set()

            for currPattern in currLevel:
                remNums, lastNum = currPattern
                for nextNum in remNums:
                    middleNum = self.middle(fromNum=lastNum, toNum=nextNum)
                    if middleNum not in remNums:
                        nextPattern = ( remNums-{nextNum}, nextNum )
                        patternCounts.setdefault( nextPattern, 0 )

                        patternCounts[ nextPattern ] += patternCounts[ currPattern ]
                        numToPattern[ nextLevelPatternLen ] += patternCounts[ currPattern ]
                        nextLevel.add( nextPattern )

            currLevel = nextLevel

        self.numToPattern = numToPattern


    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return sum(self.numToPattern[m:n+1])