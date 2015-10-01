from os.path import commonprefix
import unittest

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return commonprefix(strs)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.longestCommonPrefix(["abc", "abe", "ab"]), "ab")


if __name__ == '__main__':
    unittest.main()
