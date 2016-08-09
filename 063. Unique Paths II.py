class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        obs = 1

        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]==obs:
            return 0

        retGrid = [ [None for x in R] for R in obstacleGrid ]

        retGrid[0][0] = 1

        for i in range(1,len(obstacleGrid)):
            retGrid[i][0] = retGrid[i-1][0] if obstacleGrid[i][0]!=obs else 0

        for j in range(1,len(obstacleGrid[0])):
            retGrid[0][j] = retGrid[0][j-1] if obstacleGrid[0][j]!=obs else 0

        for i in range(1, len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==obs:
                    retGrid[i][j] = 0
                else:
                    retGrid[i][j] = retGrid[i-1][j] + retGrid[i][j-1]

        return retGrid[-1][-1]