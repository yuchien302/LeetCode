import unittest


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == "-":
            if int(s[0] + s[1:][::-1]) < -2147483648:
                return 0
            else:
                return int(s[0] + s[1:][::-1])
        else:
            if int(s[::-1]) > 2147483648:
                return 0
            else:
                return int(s[::-1])


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_1(self):
        self.assertEqual(self.solution.reverse(-123), -321)

if __name__ == '__main__':
    unittest.main()
