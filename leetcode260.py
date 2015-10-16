import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        w = 0
        for num in nums:
            w ^= num

        diff_bit = w & (-w)

        a, b = 0, 0
        for num in nums:
            if (num & diff_bit) == 0:
                a ^= num
            else:
                b ^= num

        return sorted([a, b])


class Test(unittest.TestCase):
    def test_0(self):
        self.assertListEqual(Solution().singleNumber([2,1,2,3,4,1]), [3, 4])


if __name__ == '__main__':
    unittest.main()
