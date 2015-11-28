class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        AB = [[ 0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] != 0:
                    for b in range(len(B[0])):
                        AB[r][b] += A[r][c] * B[c][b]
        return AB