class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return 
        row, col = len(matrix), len(matrix[0])
        row_0_has_0 = not all(matrix[0])
        col_0_has_0 = not all([matrix[r][0] for r in range(len(matrix))])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        for r in range(1, row):
            if matrix[r][0] == 0:
                for c in range(1, col):
                    matrix[r][c] = 0

        for c in range(1, col):
            if matrix[0][c] == 0:
                for r in range(1, row):
                    matrix[r][c] = 0


        if row_0_has_0:
            matrix[0][:] = [0] * col
            
        if col_0_has_0:
            for r in range(row):
                matrix[r][0] = 0
                    
                    