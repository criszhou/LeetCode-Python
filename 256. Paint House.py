class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        lastMinCost = [0,0,0]

        for cost in costs:
            newMinCost = [0,0,0]
            newMinCost[0] = cost[0] + min(lastMinCost[1], lastMinCost[2])
            newMinCost[1] = cost[1] + min(lastMinCost[2], lastMinCost[0])
            newMinCost[2] = cost[2] + min(lastMinCost[0], lastMinCost[1])

            lastMinCost = newMinCost

        return min(lastMinCost)