class Solution(object):
    findStrobogrammaticCache = [ [""],
                            ["0", "1", "8"],
                            ["00", "11", "88", "69", "96"], ]

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        while n >= len(self.findStrobogrammaticCache):
            nextLevel = [ s2[0] + mid + s2[1] for mid in self.findStrobogrammaticCache[-2] for s2 in self.findStrobogrammaticCache[2] ]
            self.findStrobogrammaticCache.append( nextLevel )

        return [ s for s in self.findStrobogrammaticCache[n] if n==1 or s[0]!='0' ]