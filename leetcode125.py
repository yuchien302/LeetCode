import unittest


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''.join(map(str.lower, filter(str.isalnum, str(s))))
        return new_s == new_s[::-1]


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().isPalindrome("A man, a plan, a canal: Panama"), True)


if __name__ == '__main__':
    unittest.main()
