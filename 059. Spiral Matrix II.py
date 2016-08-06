class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [ [None for j in range(n)] for i in range(n) ]

        def moveToNext( loc, dir ):
            x,y = [loc[0] + dir[0], loc[1] + dir[1]]
            if not (0<=x<n and 0<=y<n and ret[x][y] is None):
                dir[0], dir[1] = dir[1], -dir[0]

            loc[0] += dir[0]
            loc[1] += dir[1]

        location = [0,0]
        direction = [0,1]
        for num in range(1,n**2+1):
            x,y = location
            ret[x][y] = num
            moveToNext( location, direction )

        return ret