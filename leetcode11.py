import unittest


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_volumn = 0
        while right >= left:
            max_volumn = max( max_volumn, min(height[left], height[right])*(right-left) )
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_volumn


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

if __name__ == '__main__':
    unittest.main()
