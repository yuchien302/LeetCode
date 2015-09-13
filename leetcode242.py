__author__ = 'yuchien'

import unittest

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return ''.join(sorted(s)) == ''.join(sorted(t))




class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        isAnagram = self.solution.isAnagram("raphael", "aphealr")
        self.assertEqual(isAnagram, True)



if __name__ == '__main__':
    unittest.main()
