class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        sidelen = len(matrix)

        for i in range(sidelen//2):
            for j in range(sidelen - sidelen//2):
                matrix[i][j], matrix[j][-1-i], matrix[-1-i][-1-j], matrix[-1-j][i] = matrix[-1-j][i], matrix[i][j], matrix[j][-1-i], matrix[-1-i][-1-j]