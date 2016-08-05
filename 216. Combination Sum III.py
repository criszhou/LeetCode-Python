class Solution(object):
    def combinationSum3Helper(self, remNumChoices, remNumCount, remTarget, partialRes, results):
        if remTarget==0 and remNumCount==0:
            results.append( list(reversed(partialRes)) )
            return

        if remTarget<=0 or remNumCount<=0:
            return

        if not remNumChoices:
            return

        currNum = remNumChoices.pop()

        # do not add currNum
        self.combinationSum3Helper( remNumChoices, remNumCount, remTarget, partialRes, results )

        # do add currNum
        partialRes.append( currNum )
        self.combinationSum3Helper( remNumChoices, remNumCount-1, remTarget-currNum, partialRes, results )
        partialRes.pop()

        remNumChoices.append( currNum )

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []

        self.combinationSum3Helper(remNumChoices=list(range(1,10)),
                                   remNumCount = k,
                                   remTarget = n,
                                   partialRes=[],
                                   results=ret)

        return ret