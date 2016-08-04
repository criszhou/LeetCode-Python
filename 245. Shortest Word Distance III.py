class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last1 = float('-inf')
        last2 = float('-inf')

        ret = float('+inf')

        for i,w in enumerate(words):
            if w==word1:
                ret = min( ret, i-last2 )
            if w==word2:
                ret = min( ret, i-last1 )

            if w==word1:
                last1 = i
            if w==word2:
                last2 = i

        return ret
