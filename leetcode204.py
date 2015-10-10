import unittest


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2 :
            return 0

        primes = [True] * (n)
        primes[0] = primes[1] = False

        for i in range(2, int( n ** 0.5 ) + 1):
            if primes[i]:
                primes[i*i : n : i] = [False] * len(primes[i*i:n:i])

        return sum(primes)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        nums = self.solution.countPrimes(200)
        self.assertEqual(nums, 46)

if __name__ == '__main__':
    unittest.main()
