class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                liveCount = sum( (board[r][c] & 1) for r in range(row-1,row+2) for c in range(col-1,col+2)
                                 if (r,c) != (row,col) and 0<=r<len(board) and 0<=c<len(board[r]) )

                thisLive = ( board[row][col] and liveCount==2 ) or liveCount==3
                if thisLive:
                    board[row][col] |= 2


        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] >>= 1