class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return 0

        minSums = list(triangle[-1])

        # move from the bottom level up to the top level
        for i in range(len(triangle)-2,-1,-1):
            currLevel = triangle[i]

            for j,num in enumerate(currLevel):
                minSums[j] = currLevel[j] + min( minSums[j], minSums[j+1] )

            minSums.pop()

        return minSums[0]