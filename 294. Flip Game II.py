class Solution(object):
    canWinCache = dict()

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return False

        if s not in self.canWinCache:
            for i in range(len(s)-1):
                if s[i:i+2] == '++' and not self.canWin( s[:i]+'--'+s[i+2:] ):
                    ret = True
                    break
            else:
                ret = False

            self.canWinCache[s] = ret

        return self.canWinCache[s]