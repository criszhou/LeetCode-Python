class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        assert word1!=word2

        lastWord1Index = float('-inf')
        lastWord2Index = float('-inf')
        ret = float('inf')

        for i,w in enumerate(words):
            if w==word1:
                lastWord1Index = i
            elif w==word2:
                lastWord2Index = i

            ret = min( ret, abs(lastWord1Index-lastWord2Index) )
            if ret==1:
                break

        return ret