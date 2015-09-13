__author__ = 'yuchien'

import unittest

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid[0])
        row = len(grid)

        paths = [[0 for i in range(col)] for j in range(row)]
        for r in range(0, row):
            for c in range(0, col):
                if r == 0 and c == 0:
                    paths[r][c] = grid[r][c]
                elif r == 0 and c != 0:
                    paths[r][c] = paths[r][c - 1] + grid[r][c]
                elif r != 0 and c == 0:
                    paths[r][c] = paths[r - 1][c] + grid[r][c]
                else:
                    paths[r][c] = min(paths[r][c - 1], paths[r - 1][c]) + grid[r][c]
        # print(grid)
        return paths[row-1][col-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        paths = self.solution.minPathSum([[0]])
        self.assertEqual(paths, 0)

    def test_2(self):
        paths = self.solution.minPathSum([[1]])
        self.assertEqual(paths, 1)

    def test_3(self):
        paths = self.solution.minPathSum([[0, 3, 1]])
        self.assertEqual(paths, 4)

    def test_4(self):
        paths = self.solution.minPathSum([[0], [3], [4]])
        self.assertEqual(paths, 7)

    def test_5(self):
        paths = self.solution.minPathSum([[0, 3, 2], [1, 5, 1]])
        self.assertEqual(paths, 6)

if __name__ == '__main__':
    unittest.main()
