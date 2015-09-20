import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)

        return len(nums)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        lists = [0]
        nums = self.solution.removeElement(lists, 0)
        self.assertEqual(nums, 0)

    def test_1(self):
        lists = [4, 5]
        nums = self.solution.removeElement(lists, 4)
        self.assertEqual(nums, 1)

if __name__ == '__main__':
    unittest.main()
