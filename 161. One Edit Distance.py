class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s)-len(t))>=2:
            return False

        if len(s) > len(t):
            t,s = s,t

        # now t is longer than s, or same length
        if len(s) == len(t):
            return sum( 1 for i in range(len(s)) if s[i]!=t[i] ) == 1

        if len(s)+1 == len(t):
            si, ti = 0, 0
            while si<=ti<=si+1<len(t):
                if s[si] == t[ti]:
                    si += 1
                    ti += 1
                else:
                    ti += 1

            return si+1==ti==len(t) or si==ti==len(s)

        assert False