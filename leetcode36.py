import unittest


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        square = [[False]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if row[r][int(board[r][c])-1]:
                        return False
                    if col[c][int(board[r][c])-1]:
                        return False
                    if square[3 * int(r/3) + int(c/3)][int(board[r][c])-1]:
                        return False

                    row[r][int(board[r][c])-1] = True
                    col[c][int(board[r][c])-1] = True
                    square[3 * int(r/3) + int(c/3)][int(board[r][c])-1] = True

        return True


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        is_valid = self.solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(is_valid, True)

if __name__ == '__main__':
    unittest.main()
