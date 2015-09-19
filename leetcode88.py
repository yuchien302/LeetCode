import unittest


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        idx1 = 0
        idx2 = 0
        temp1 = nums1[:m]
        for i in range(m+n):
            if idx1 >= m:
                nums1[i] = nums2[idx2]
                idx2 += 1
            elif idx2 >= n:
                nums1[i] = temp1[idx1]
                idx1 += 1
            elif temp1[idx1] < nums2[idx2]:
                nums1[i] = temp1[idx1]
                idx1 += 1
            else:
                nums1[i] = nums2[idx2]
                idx2 += 1


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        nums1 = [1]
        nums2 = []
        self.solution.merge(nums1, len(nums1), nums2, len(nums2))
        self.assertListEqual(nums1, [1])

    def test_1(self):
        nums1 = [1, 1, 3, 5, 0, 0, 0]
        nums2 = [2, 4, 6]
        self.solution.merge(nums1, 4, nums2, len(nums2))
        self.assertListEqual(nums1, [1, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
