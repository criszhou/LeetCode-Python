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

        # binary search, find which row target is in

        minRow = 0
        maxRow = numRows-1

        while maxRow - minRow > 3:
            midRow = (maxRow + minRow) // 2
            if target < matrix[midRow][0]:
                maxRow = midRow - 1
            elif target > matrix[midRow][-1]:
                minRow = midRow + 1
            else:
                maxRow = midRow
                minRow = midRow

        for r in range(minRow, maxRow+1):
            if matrix[r][0] <= target <= matrix[r][-1]:
                rowNums = matrix[r]
                break
        else:
            return False

        # now that target can only exist in rowNums, use binary search to find it

        minCol = 0
        maxCol = numCols - 1

        while maxCol - minCol > 3:
            midCol = (maxCol + minCol) // 2
            if target < rowNums[midCol]:
                maxCol = midCol - 1
            elif target > rowNums[midCol]:
                minCol = midCol + 1
            else:
                return True

        return target in rowNums[minCol:maxCol+1]