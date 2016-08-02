class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False

        stack = []
        validPairs = ( "()", "[]", "{}" )

        for c in s:
            if c in "{[(":
                stack.append( c )
            elif stack and (stack[-1]+c) in validPairs:
                stack.pop()
            else:
                return False

        return not stack