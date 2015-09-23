import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")

if __name__ == '__main__':
    unittest.main()
