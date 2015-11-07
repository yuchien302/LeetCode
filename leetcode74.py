class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col
        while low < high:
            mid = int((low + high) / 2)
            c = mid % col
            r = mid // col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid
                
        return False
        