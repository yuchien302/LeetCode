class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = [], []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
        
        rows.sort()
        cols.sort()
        mr = rows[len(rows)//2]
        mc = cols[len(cols)//2]

        return sum( abs(r-mr) for r in rows ) + sum( abs(c-mc) for c in cols )