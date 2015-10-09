import unittest
from operator import add


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        temp = [1, 1]

        for i in range(1, rowIndex):
            arr1 = temp + [0]
            arr2 = [0] + temp
            temp = list(map(add, arr1, arr2))

        return temp



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        results = self.solution.getRow(3)
        self.assertListEqual(results, [1,3,3,1])


if __name__ == '__main__':
    unittest.main()
