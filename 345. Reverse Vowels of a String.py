class Solution(object):
    vowels = set( "aeiouAEIOU" )

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        retList = list(s)
        p1 = 0
        p2 = len(s)-1
        
        while p1<p2:
            if s[p1] not in self.vowels:
                p1 += 1
            elif s[p2] not in self.vowels:
                p2 -= 1
            else:
                retList[p1], retList[p2] = retList[p2], retList[p1]
                p1 += 1
                p2 -= 1

        return "".join(retList)