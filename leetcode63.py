import unittest


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        col = len(obstacleGrid[0])
        row = len(obstacleGrid)

        paths = [[0 for i in range(col)] for j in range(row)]
        for r in range(0, row):
            for c in range(0, col):
                if obstacleGrid[r][c] == 0:
                    if r == 0 and c == 0:
                        paths[r][c] = 1
                    elif r == 0 and c != 0:
                        paths[r][c] = paths[r][c - 1]
                    elif r != 0 and c == 0:
                        paths[r][c] = paths[r - 1][c]
                    else:
                        paths[r][c] = paths[r][c - 1] + paths[r - 1][c]
        # print(paths)
        return paths[row-1][col-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_corner1(self):
        paths = self.solution.uniquePathsWithObstacles([[0]])
        self.assertEqual(paths, 1)

    def test_corner2(self):
        paths = self.solution.uniquePathsWithObstacles([[1]])
        self.assertEqual(paths, 0)

    def test_corner3(self):
        paths = self.solution.uniquePathsWithObstacles([[0, 0, 0]])
        self.assertEqual(paths, 1)

    def test_corner4(self):
        paths = self.solution.uniquePathsWithObstacles([[0, 1, 0]])
        self.assertEqual(paths, 0)

    def test_corner5(self):
        paths = self.solution.uniquePathsWithObstacles([[0], [0], [0]])
        self.assertEqual(paths, 1)

    def test_corner6(self):
        paths = self.solution.uniquePathsWithObstacles([[0], [1], [0]])
        self.assertEqual(paths, 0)

    def test_corner7(self):
        paths = self.solution.uniquePathsWithObstacles([[0, 0], [0, 0]])
        self.assertEqual(paths, 2)

if __name__ == '__main__':
    unittest.main()
