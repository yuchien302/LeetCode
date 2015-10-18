import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)

    def test_1(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)

    def test_2(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 7), 4)

    def test_3(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 0), 0)

if __name__ == '__main__':
    unittest.main()
