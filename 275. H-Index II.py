class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations or citations[-1]==0:
            return 0

        if citations[0] >= len(citations):
            return len(citations)

        Min = 1
        Max = len(citations)-1

        while Min < Max-3:
            Mid = (Max+Min)//2

            if citations[-Mid] >= Mid:
                Min = Mid
            else:
                Max = Mid-1

        for ret in range(Max,Min-1,-1):
            if citations[-ret] >= ret:
                return ret