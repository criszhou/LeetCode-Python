class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""

        if len(strs)==1:
            return strs[0]

        minLength = min( len(s) for s in strs )

        for i in range(minLength):
            if len( { s[i] for s in strs } ) > 1:
                return strs[0][:i]

        return strs[0][:minLength]