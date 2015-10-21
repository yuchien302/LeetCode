class Solution(object):
    def found(self, board, word, r, c):
        if word == "":
            return True
        
        row = len(board)
        col = len(board[0])
        
        if not ( 0 <= r < row and 0 <= c < col and board[r][c] == word[0]):
           return False
        else:
            cur = board[r][c]
            board[r][c] = '#'
            founded =  (self.found(board, word[1:], r-1, c) or
                   self.found(board, word[1:], r, c-1) or
                   self.found(board, word[1:], r+1, c) or
                   self.found(board, word[1:], r, c+1))
            board[r][c] = cur
            return founded
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == "":
            return True
            
        if len(board) == 0:
            return False
            
        row = len(board)
        col = len(board[0])
        
        for r in range(row):
            for c in range(col):
                if self.found(board, word, r, c):
                    return True
        return False
        