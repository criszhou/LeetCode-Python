class Solution(object):
    def hasDuplicate(self, iterable):
        seenSet = set()
        for x in iterable:
            if x != '.':
                if x in seenSet:
                    return True
                seenSet.add( x )
        return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            if self.hasDuplicate( board[row][col] for col in range(9) ):
                return False

        for col in range(9):
            if self.hasDuplicate( board[row][col] for row in range(9) ):
                return False

        for row in [0,3,6]:
            for col in [0,3,6]:
                if self.hasDuplicate( board[row+i][col+j] for i in range(3) for j in range(3) ):
                    return False

        return True