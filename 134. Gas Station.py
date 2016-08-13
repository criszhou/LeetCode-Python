class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1

        ret = 0
        retLevel = 0
        currLevel = 0

        for i,(g,c) in enumerate(zip(gas,cost)):
            if currLevel < retLevel:
                ret = i
                retLevel = currLevel

            currLevel += (g-c)

        return ret