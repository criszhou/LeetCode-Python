from itertools import chain

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()
        lastWordBegin = 0
        for i,c in enumerate( chain( s, " " ) ):
            if c==' ':
                p1, p2 = lastWordBegin, i-1
                while p1<p2:
                    s[p1], s[p2] = s[p2], s[p1]
                    p1 += 1
                    p2 -= 1

                lastWordBegin = i + 1