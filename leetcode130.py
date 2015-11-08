from collections import deque
class Solution(object):
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        
        saves = deque()
        
        for r in range(len(board)):
            saves.append((r, 0))
            saves.append((r, len(board[0])-1))
            
        for c in range(len(board[0])):  
            saves.append((0, c))
            saves.append((len(board)-1, c))

        while len(saves) != 0:
            r, c = saves.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = '#'
                saves.append((r-1, c))
                saves.append((r, c-1))
                saves.append((r+1, c))
                saves.append((r, c+1))
                
        board[:] = [[ 'X' if board[r][c] != '#' else 'O' for c in range(len(board[0]))] for r in range(len(board))]
        