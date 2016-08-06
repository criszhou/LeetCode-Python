from collections import Counter

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        Max = len(citations)

        citToCount = Counter( min(Max,cit) for cit in citations )

        GECount = 0 # count the number of citations which are greater than equal to current number
        for ret in range(Max,-1,-1):
            GECount += citToCount[ret]

            if GECount >= ret:
                return ret