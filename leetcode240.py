class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = len(matrix)-1, 0
        if r < 0:
            return False
            
        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] < target:
                c += 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                return True
            
        return False