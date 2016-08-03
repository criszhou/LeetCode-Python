class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        reversedRet = [0] * (1 + max(len(a), len(b)))

        for i, c in enumerate(reversed(a)):
            reversedRet[i] += (c == '1')
        for i, c in enumerate(reversed(b)):
            reversedRet[i] += (c == '1')

        for i in range(len(reversedRet)):
            if reversedRet[i] >= 2:
                reversedRet[i] -= 2
                reversedRet[i + 1] += 1

        while len(reversedRet) > 1 and reversedRet[-1] == 0:
            reversedRet.pop()

        return "".join(str(x) for x in reversed(reversedRet))