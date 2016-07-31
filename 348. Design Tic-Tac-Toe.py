class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rowMoveCount1 = [0] * n # maps k to how many pos in row k are occupied by player 1
        self.rowMoveCount2 = [0] * n # maps k to how many pos in row k are occupied by player 2
        self.colMoveCount1 = [0] * n # maps k to how many pos in col k are occupied by player 1
        self.colMoveCount2 = [0] * n # maps k to how many pos in col k are occupied by player 2
        self.mainDiagMoveCount1 = [0] # how many pos in main diag (row==col) are occupied by player 1
        self.mainDiagMoveCount2 = [0] # how many pos in main diag (row==col) are occupied by player 2
        self.antiDiagMoveCount1 = [0] # how many pos in anti diag (row+col==n-1) are occupied by player 1
        self.antiDiagMoveCount2 = [0] # how many pos in anti diag (row+col==n-1) are occupied by player 2

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        assert player==1 or player==2

        rowCountList = self.rowMoveCount1 if player==1 else self.rowMoveCount2
        colCountList = self.colMoveCount1 if player==1 else self.colMoveCount2
        mainDiagCountList = self.mainDiagMoveCount1 if player==1 else self.mainDiagMoveCount2
        antiDiagCountList = self.antiDiagMoveCount1 if player==1 else self.antiDiagMoveCount2

        rowCountList[row] += 1
        colCountList[col] += 1
        if row == col:
            mainDiagCountList[0] += 1
        if row + col == self.n - 1:
            antiDiagCountList[0] += 1

        if self.n in [ rowCountList[row], colCountList[col], mainDiagCountList[0], antiDiagCountList[0] ]:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)