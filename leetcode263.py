import unittest


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False

        while num % 2 == 0:
            num /= 2

        while num % 3 == 0:
            num /= 3

        while num % 5 == 0:
            num /= 5

        if num == 1:
            return True
        else:
            return False


class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(Solution().isUgly(-51799), False)

if __name__ == '__main__':
    unittest.main()
