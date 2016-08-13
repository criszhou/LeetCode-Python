class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        # find min and max of x-coord
        minX = float("+inf")
        maxX = float("-inf")
        for x,y in points:
            if x<minX:
                minX = x
            if x>maxX:
                maxX = x
        midXx2 = minX + maxX

        pointSet = { (x,y) for x,y in points }
        for (x,y) in pointSet:
            if (midXx2-x,y) not in pointSet:
                return False

        return True