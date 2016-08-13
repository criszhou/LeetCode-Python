import collections

class Solution(object):
    def partitionHelper(self, s, currIndex, palBeginToEnd, partialRes, results):
        if currIndex==len(s):
            results.append( list(partialRes) )
            return

        for nextIndex in palBeginToEnd[currIndex]:
            partialRes.append( s[currIndex:nextIndex] )
            self.partitionHelper( s, nextIndex, palBeginToEnd, partialRes, results )
            partialRes.pop()


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # find all (i,j) such that s[i:j] is pal
        palBeginToEnd = collections.defaultdict(list)

        for mid in range(len(s)):
            begin = mid
            end = mid + 1
            palBeginToEnd[begin].append(end)
            while begin-1>=0 and end<len(s) and s[begin-1]==s[end]:
                begin -= 1
                end += 1
                palBeginToEnd[begin].append(end)

        for midAfter in range(len(s)-1):
            begin = midAfter + 1
            end = midAfter + 1
            while begin-1>=0 and end<len(s) and s[begin-1]==s[end]:
                begin -= 1
                end += 1
                palBeginToEnd[begin].append(end)

        # test
        # for i in range(len(s)+1):
        #     for j in range(i+1, len(s)+1):
        #         sub = s[i:j]
        #         print(sub)
        #         assert (j in palBeginToEnd[i]) == (sub==sub[::-1])

        print(palBeginToEnd)

        ret = []
        self.partitionHelper(s, currIndex=0, palBeginToEnd=palBeginToEnd, partialRes=[], results=ret)
        return ret