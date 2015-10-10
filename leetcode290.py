import unittest


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        table = {}
        revtable = {}
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in table and strs[i] not in revtable:
                table[pattern[i]] = strs[i]
                revtable[strs[i]] = pattern[i]
            elif pattern[i] in table and strs[i] not in revtable:
                return False
            elif pattern[i] not in table and strs[i] in revtable:
                return False
            else:
                if revtable[table[pattern[i]]] != pattern[i]:
                    return False
        return True


    def wordPattern2(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(" ")
        return map(pattern.find, pattern) == map(strs.index, strs)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        result = self.solution.wordPattern("abba", "dog cat cat dog")
        self.assertEqual(result, True)

    def test_1(self):
        result = self.solution.wordPattern("abba", "dog cat cat cow")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
