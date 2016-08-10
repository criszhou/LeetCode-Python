from collections import Counter
from itertools import chain

class Solution(object):
    def generatePalindromesPerm(self, half, fixedBefore, midChar, results):
        if fixedBefore==len(half):
            results.append( "".join( chain( half, midChar, reversed(half) ) ) )
            return

        swappedChars = set()
        for i in range(fixedBefore, len(half)):
            if half[i] not in swappedChars:
                half[fixedBefore], half[i] = half[i], half[fixedBefore]
                self.generatePalindromesPerm(half, fixedBefore+1, midChar, results)
                half[fixedBefore], half[i] = half[i], half[fixedBefore]

                swappedChars.add( half[i] )

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        charCounter = Counter(s)

        half = []
        mid = ""
        for char,count in charCounter.items():
            if count%2==1:
                if mid =="":
                    mid = char
                else:
                    return []

            half.extend( [char] * (count//2) )

        ret = []
        self.generatePalindromesPerm(half, fixedBefore=0, midChar=mid, results=ret)
        return ret