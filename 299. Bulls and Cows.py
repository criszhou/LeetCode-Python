from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0

        cowCount1 = Counter()
        cowCount2 = Counter()

        assert len(secret)==len(guess)

        for c1,c2 in zip(secret,guess):
            if c1==c2:
                bull += 1
            else:
                cowCount1[c1] += 1
                cowCount2[c2] += 1

        cowCount = cowCount1 & cowCount2
        cow = sum( cowCount.values() )

        return str(bull) + 'A' + str(cow) + 'B'