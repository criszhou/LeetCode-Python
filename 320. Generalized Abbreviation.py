class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = [ ("",0) ] # each item is a pair (string,k) where k is the number of letters not captured in string

        for c in word:
            newRet = []
            for (s,k) in ret:
                newRet.append( (s,k+1) )
                newRet.append( (s + (str(k) if k else "") + c, 0) )

            ret = newRet

        return [ (s + (str(k) if k else "")) for (s,k) in ret ]