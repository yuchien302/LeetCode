import unittest


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return max(count, key=count.get)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.majorityElement([1, 1, 2, 5, 6, 7, 6, 6, 6, 6, 2, 6, 6, 6, 6]), 6)


if __name__ == '__main__':
    unittest.main()
