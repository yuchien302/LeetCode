import unittest


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if len(s) == 1 or s == s[::-1]:
            result.append([s])

        for i in reversed(range(1, len(s))):
            if s[:i] == s[:i][::-1]:
                restLists = self.partition(s[i:])
                for restList in restLists:
                    result.append( [s[:i]] + restList )

        return result


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        partitions = self.solution.partition("aab")
        self.assertEqual(partitions, [["aa","b"],["a","a","b"]])

    def test_1(self):
        partitions = self.solution.partition("aa")
        self.assertEqual(partitions, [["aa"],["a","a"]])


if __name__ == '__main__':
    unittest.main()
