class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        mat = [[0 for _ in range(n)] for _ in range(n)]
        colLeft, colRight = 0, n-1
        rowTop, rowBottom = 0, n-1
        count = 1
        while count <= n*n:
            for i in range(colLeft, colRight+1):
                # print(rowTop, i, count)
                mat[rowTop][i] = count
                count += 1
            rowTop += 1

            if count > n*n: break
            for i in range(rowTop, rowBottom+1):
                # print(i, colRight, count)
                mat[i][colRight] = count
                count += 1
            colRight -= 1

            if count > n*n: break
            for i in range(colRight, colLeft-1, -1):
                # print(rowBottom, i, count)
                mat[rowBottom][i] = count
                count += 1
            rowBottom -= 1


            if count > n*n: break
            for i in range(rowBottom, rowTop-1, -1):
                # print(i, colLeft, count)
                mat[i][colLeft] = count
                count += 1
            colLeft += 1

        return mat