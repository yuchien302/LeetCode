import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos_dict = {}
        longest_len = 0
        start = -1
        for i in range(len(s)):
            if s[i] in pos_dict:
                start = max(start, pos_dict[s[i]])
            pos_dict[s[i]] = i
            longest_len = max(longest_len, i - start)

        return longest_len


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaa"), 1)

    def test_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("c"), 1)

    def test_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abba"), 2)

    def test_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabca"), 3)

if __name__ == '__main__':
    unittest.main()
