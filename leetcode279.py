import unittest


class Solution(object):

    _mem = [0, 1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        _mem = self._mem

        if n < len(_mem):
            return _mem[n]


        for i in range(len(_mem), (n+1)):
            _mem.append(i)
            for j in range(2, int(sqrt(i))+1):
                if j*j <= i:
                    _mem[i] = min( _mem[i], 1 + _mem[i-j*j] )

        return _mem[n]



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        num = self.solution.numSquares(12)
        self.assertEqual(num, 3)

    def test_1(self):
        num = self.solution.numSquares(13)
        self.assertEqual(num, 2)

    def test_2(self):
        num = self.solution.numSquares(0)
        self.assertEqual(num, 0)

    def test_3(self):
        num = self.solution.numSquares(7)
        self.assertEqual(num, 4)

    def test_4(self):
        num = self.solution.numSquares(7217)
        self.assertEqual(num, 3)

    def test_5(self):
        num = self.solution.numSquares(6730)
        self.assertEqual(num, 2)


if __name__ == '__main__':
    unittest.main()


