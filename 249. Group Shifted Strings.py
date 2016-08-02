from collections import defaultdict

class Solution(object):
    def shiftStr(self, s):
        """
        shift s such that s[0]=='a'
        """
        if not s or s[0]=='a':
            return s

        moveBack = ord(s[0])-ord('a')
        return "".join( chr( ord(c)-moveBack if c>=s[0] else ord(c)-moveBack+26 ) for c in s )


    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        groupToStrings = defaultdict(list) # key is the shifted string starting at 'a', value is list of string

        for s in strings:
            groupToStrings[ self.shiftStr(s) ].append( s )

        return list( groupToStrings.values() )
