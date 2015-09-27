import unittest


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = []
        steps.append(1)
        steps.append(1)
        for i in range(2, n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.climbStairs(3), 3)


if __name__ == '__main__':
    unittest.main()
