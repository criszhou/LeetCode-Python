class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapST = dict()
        mapTS = dict()

        for cs,ct in zip(s,t):
            mapST.setdefault( cs, ct )
            mapTS.setdefault( ct, cs )

            if mapST[cs] != ct or mapTS[ct] != cs:
                return False

        return True