class Solution(object):
    
    def sink(self, r, c, grid):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
            grid[r][c] = '0'
            self.sink(r-1, c, grid)
            self.sink(r, c-1, grid)
            self.sink(r, c+1, grid)
            self.sink(r+1, c, grid)
            return 1
        return 0
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        return sum([self.sink(r, c, grid)
                    for r in range(len(grid))
                    for c in range(len(grid[0]))])
        
                
            