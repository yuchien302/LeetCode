import unittest

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        int_char = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans_str = ""
        while n != 0:
            if n % 26 != 0:
                ans_str = int_char[n % 26] + ans_str
            else:
                ans_str = int_char[26] + ans_str
            n = (n-1) // 26

        return ans_str


class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(Solution().convertToTitle(26), "Z")

    def test_1(self):
        self.assertEqual(Solution().convertToTitle(27), "AA")

if __name__ == '__main__':
    unittest.main()
