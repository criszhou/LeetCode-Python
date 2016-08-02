class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type strings: str
        :rtype: bool
        """
        strings = string.split()

        if len(pattern) != len(strings):
            return False

        mapPS = dict()
        mapSP = dict()

        for p,s in zip(pattern,strings):
            mapPS.setdefault(p,s)
            mapSP.setdefault(s,p)

            if mapSP[s]!=p or mapPS[p]!=s:
                return False

        return True