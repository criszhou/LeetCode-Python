class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.wordToIndices = dict() # map a word to its indices in words
        for i,w in enumerate(words):
            self.wordToIndices.setdefault( w, [] )
            self.wordToIndices[ w ].append( i )

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indices1 = self.wordToIndices[ word1 ]
        indices2 = self.wordToIndices[ word2 ]

        i1, i2 = 0, 0
        ret = float("inf")

        # find the minimum difference from two sorted lists. Use two pointers
        while i1<len(indices1) and i2<len(indices2):
            ret = min( ret, abs( indices1[i1] - indices2[i2] ) )

            if ret == 1:
                return 1

            if indices1[i1] < indices2[i2]:
                i1 += 1
            else:
                i2 += 1

        return ret



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")