import unittest


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                break
            idx += 1

        for i in range(idx, len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                nums[i] = 0
                idx += 1



class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        lists = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(lists)
        self.assertListEqual(lists, [1, 3, 12, 0, 0])

    def test_1(self):
        lists = [1]
        self.solution.moveZeroes(lists)
        self.assertListEqual(lists, [1])

    def test_2(self):
        lists = [1, 0]
        self.solution.moveZeroes(lists)
        self.assertListEqual(lists, [1, 0])

if __name__ == '__main__':
    unittest.main()
