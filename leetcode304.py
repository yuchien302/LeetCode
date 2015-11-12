class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.matrix_sum = [[matrix[r][c] for c in range(len(matrix[0]))] for r in range(len(matrix))]
        for r in range(1, len(matrix)):
            self.matrix_sum[r][0] = self.matrix_sum[r-1][0] + matrix[r][0] 
        for c in range(1, len(matrix[0])):
            self.matrix_sum[0][c] = self.matrix_sum[0][c-1] + matrix[0][c]
            
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                self.matrix_sum[r][c] = self.matrix_sum[r][c-1] + self.matrix_sum[r-1][c] + matrix[r][c] - self.matrix_sum[r-1][c-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
         
        if row1 == col1 == 0:
            return self.matrix_sum[row2][col2]
        elif row1 == 0:
            return self.matrix_sum[row2][col2] - self.matrix_sum[row2][col1-1]
        elif col1 == 0:
            return self.matrix_sum[row2][col2] - self.matrix_sum[row1-1][col2]
        else:
            return (self.matrix_sum[max(row1, row2)][max(col1, col2)] - 
                    self.matrix_sum[max(0, min(row1, row2)-1)][max(col1, col2)] - 
                    self.matrix_sum[max(row1, row2)][max(0, min(col1, col2)-1)] + 
                    self.matrix_sum[max(0, min(row1, row2)-1)][max(0, min(col1, col2)-1)])



# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)