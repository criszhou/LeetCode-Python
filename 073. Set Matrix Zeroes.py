class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        firstRowHasZero = any( x==0 for x in matrix[0] )

        for i in range(1,len(matrix)):
            thisRowHasZero = False

            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    thisRowHasZero = True
                    matrix[0][j] = 0

            if thisRowHasZero:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0

        if firstRowHasZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0