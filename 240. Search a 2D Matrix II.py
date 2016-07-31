class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        numRows = len(matrix)
        numCols = len(matrix[0])

        row = 0
        col = numCols-1

        while 0<=row<numRows and 0<=col<numCols:
            thisNum = matrix[row][col]
            if thisNum < target:
                row += 1
            elif thisNum > target:
                col -= 1
            else:
                return True

        return False