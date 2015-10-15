import unittest


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        if (min(C, G) - max(A, E)) < 0 or (min(D, H) - max(B, F)) < 0:
            return (C - A) * (D - B) + (G - E) * (H - F)

        return (C - A) * (D - B) + (G - E) * (H - F) - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2), 16)


if __name__ == '__main__':
    unittest.main()
