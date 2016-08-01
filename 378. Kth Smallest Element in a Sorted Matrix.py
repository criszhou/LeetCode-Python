class Solution(object):
    def getMatrixCell(self, matrix, row, col, reverse):
        """
        if reverse, row and col counts
        """
        if reverse:
            return -matrix[-1-row][-1-col]
        else:
            return matrix[row][col]

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        k -= 1

        from heapq import heappush, heappop

        numRows = len(matrix)
        numCols = len(matrix[0])

        # if k is large, we view matrix reversely i.e. upside-down and left-right reversed, also add a minus sign so we can still use a min-heap
        reverse = False
        if k > numRows * numCols // 2:
            k = numRows * numCols - 1 - k
            reverse = True

        seenCells = {(0, 0)}  # item has format (i,j), meaning matrix[i][j] is seen
        heap = [
            (self.getMatrixCell(matrix, 0, 0, reverse=reverse), 0, 0)]  # each heap item is a 3-tuple, (num, row, col)

        # Start heap-sort
        for it in range(k + 1):
            num, row, col = heappop(heap)

            if it == k:
                break

            if col + 1 < numCols and (row, col + 1) not in seenCells:
                seenCells.add((row, col + 1))
                heappush(heap, (self.getMatrixCell(matrix, row, col + 1, reverse=reverse), row, col + 1))

            if row + 1 < numRows and (row + 1, col) not in seenCells:
                seenCells.add((row + 1, col))
                heappush(heap, (self.getMatrixCell(matrix, row + 1, col, reverse=reverse), row + 1, col))

        return -num if reverse else num
