from copy import deepcopy

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sumGrid = deepcopy( grid )

        for j in range(1,len(grid[0])):
            sumGrid[0][j] += sumGrid[0][j-1]

        for i in range(1,len(grid)):
            sumGrid[i][0] += sumGrid[i-1][0]

        for i in range(1, len(grid)):
            for j in range(1,len(grid[0])):
                sumGrid[i][j] += min( sumGrid[i-1][j],sumGrid[i][j-1] )

        return sumGrid[-1][-1]