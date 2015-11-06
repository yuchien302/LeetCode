class Solution(object):
    def walk(self, dist, r, c, rooms):
        
        row = len(rooms)
        col = len(rooms[0])
        if not (0 <= r < row and 0 <= c < col):
            return
        
        if rooms[r][c] < dist:
            return
        
        rooms[r][c] = dist
        
        self.walk(dist+1, r-1, c, rooms)
        self.walk(dist+1, r+1, c, rooms)
        self.walk(dist+1, r, c-1, rooms)
        self.walk(dist+1, r, c+1, rooms)
    
    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    self.walk(0, r, c, rooms)
        return
                    