class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrevToWord = dict() # maps abbrev to its original word
        self.multiWordAbbrev = set() # set of abbrevs with multiple words

        for w in dictionary:
            abbrev = self.getAbbrev(w)
            if abbrev not in self.multiWordAbbrev:
                if abbrev not in self.abbrevToWord:
                    self.abbrevToWord[abbrev] = w
                elif self.abbrevToWord[abbrev] != w:
                    del self.abbrevToWord[abbrev]
                    self.multiWordAbbrev.add(abbrev)

    def getAbbrev(self, word):
        if len(word)>2:
            word = word[0] + str(len(word)-2) + word[-1]
        return word

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbrev = self.getAbbrev(word)

        return ( abbrev not in self.multiWordAbbrev ) and ( abbrev not in self.abbrevToWord or self.abbrevToWord[abbrev] == word )



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")