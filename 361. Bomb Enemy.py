class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        wall  = 'W'
        enemy = 'E'
        empty = '0'

        numRows = len(grid)
        numCols = len(grid[0])

        # for each empty cell, how many enemies in the same row will be killed if bomb there
        rowKillCount = [ [ 0 for j in range(numCols) ] for i in range(numRows) ]
        # for each empty cell, how many enemies in the same col will be killed if bomb there
        colKillCount = [ [ 0 for j in range(numCols) ] for i in range(numRows) ]

        # calc rowKillCount
        for i in range(numRows):
            emptyCols = []
            killCount = 0

            for j in range(numCols+1):
                if j==numCols or grid[i][j] == wall:
                    for emptyCol in emptyCols:
                        rowKillCount[i][emptyCol] = killCount
                    killCount = 0
                    emptyCols = []
                elif grid[i][j] == enemy:
                    killCount += 1
                elif grid[i][j] == empty:
                    emptyCols.append( j )

        # calc colKillCount
        for j in range(numCols):
            emptyRows = []
            killCount = 0

            for i in range(numRows + 1):
                if i == numRows or grid[i][j] == wall:
                    for emptyRow in emptyRows:
                        colKillCount[emptyRow][j] = killCount
                    killCount = 0
                    emptyRows = []
                elif grid[i][j] == enemy:
                    killCount += 1
                elif grid[i][j] == empty:
                    emptyRows.append(i)

        # find max of rolKillCount and colKillCount
        ret = 0
        for i in range(numRows):
            for j in range(numCols):
                ret = max( ret, rowKillCount[i][j] + colKillCount[i][j] )
        return ret