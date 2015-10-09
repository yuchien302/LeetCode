import unittest
from operator import add


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        result = [[1]]

        for i in range(1, numRows):
            arr1 = result[i-1] + [0]
            arr2 = [0] + result[i-1]
            arr = list(map(add, arr1, arr2))
            result.append(arr)

        return result



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        results = self.solution.generate(3)

        self.assertListEqual(results, [[1], [1, 1], [1, 2, 1]])


if __name__ == '__main__':
    unittest.main()
