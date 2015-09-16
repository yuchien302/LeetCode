import unittest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        pal = self.solution.plusOne([1, 0, 1, 1, 9])
        self.assertListEqual(pal, [1, 0, 1, 2, 0])

    def test_1(self):
        pal = self.solution.plusOne([9])
        self.assertListEqual(pal, [1, 0])



if __name__ == '__main__':
    unittest.main()


__author__ = 'yuchien'
