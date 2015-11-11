class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])

        colLeft = rowTop = 0
        colRight = col - 1
        rowBottom = row - 1
        n = row * col
        res = []
        while rowTop <= rowBottom and colLeft <= colRight:

            for c in range( colLeft, colRight+1 ):
                res.append(matrix[rowTop][c])
            rowTop += 1
            
            for r in range( rowTop, rowBottom+1 ):
                res.append(matrix[r][colRight])
            colRight -= 1
            
            if rowTop <= rowBottom:
                for c in range( colRight, colLeft-1, -1 ):
                    res.append(matrix[rowBottom][c])
                rowBottom -= 1
                
            if colLeft <= colRight:
                for r in range( rowBottom, rowTop-1, -1 ):
                    res.append(matrix[r][colLeft])
                colLeft += 1            
            
        return res
            