class Solution(object):
    def combinationSumHelper(self, remCandidates, remTarget, partialRes, results):
        if remTarget==0:
            results.append( list(partialRes) )
            return

        if remTarget<0:
            return

        if not remCandidates:
            return

        currCand = remCandidates[-1]

        # use currCand
        partialRes.append( currCand )
        self.combinationSumHelper( remCandidates, remTarget-currCand, partialRes, results)
        partialRes.pop()

        # don't use currCand
        remCandidates.pop()
        self.combinationSumHelper( remCandidates, remTarget, partialRes, results)
        remCandidates.append( currCand )



    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.combinationSumHelper(candidates, target, [], ret)
        return ret