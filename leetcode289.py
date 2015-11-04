class Solution(object):
    def update(self, board, r, c):
        count = 0
        row, col = len(board)-1, len(board[0])-1
        
        if r > 0 and c > 0:     count += (board[r-1][c-1] % 2)
        if c > 0:               count += (board[r][c-1] % 2)
        if r < row and c > 0:   count += (board[r+1][c-1] % 2)
        if r > 0:               count += (board[r-1][c] % 2)
        if r < row:             count += (board[r+1][c] % 2)
        if r > 0 and c < col:   count += (board[r-1][c+1] % 2)
        if c < col:             count += (board[r][c+1] % 2)
        if r < row and c < col: count += (board[r+1][c+1] % 2)
        
        if count < 2 and board[r][c] == 1:
            board[r][c] = 3

        if count > 3 and board[r][c] == 1:
            board[r][c] = 3
            
        if count == 3 and board[r][c] == 0:
            board[r][c] = 2
            
        
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0: 
            return
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.update(board, r, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2:
                    board[r][c] = 1
                if board[r][c] == 3:
                    board[r][c] = 0    
        