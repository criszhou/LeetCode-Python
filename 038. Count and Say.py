class Solution(object):
    countAndSayResults = ["1"]

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1

        while n >= len(self.countAndSayResults):
            lastResult = self.countAndSayResults[-1]
            newResultList = []

            lastChar = None
            lastCharCount = 0

            for c in lastResult:
                if c != lastChar:
                    if lastCharCount > 0:
                        newResultList.append(str(lastCharCount) + lastChar)
                    lastChar = c
                    lastCharCount = 1
                else:
                    lastCharCount += 1

            newResultList.append(str(lastCharCount) + lastChar)

            self.countAndSayResults.append("".join(newResultList))

        return self.countAndSayResults[n]