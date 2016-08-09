class Solution(object):
    buttonToLetters = { str(i):s for i,s in enumerate([" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]) }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        ret = [ "" ]
        for c in digits:
            ret = [ a+b for b in self.buttonToLetters[c] for a in ret ]
        return ret