class Solution(object):
    def sink(self, image, x, y, bounds):
        row = len(image)
        col = len(image[0])
        if 0 <= x < row and 0 <= y < col and image[x][y] == '1':
            image[x][y] = '0'
            self.sink(image, x-1, y, bounds)
            self.sink(image, x+1, y, bounds)
            self.sink(image, x, y-1, bounds)
            self.sink(image, x, y+1, bounds)
            bounds[0] = min(bounds[0], x)
            bounds[1] = max(bounds[1], x)
            bounds[2] = min(bounds[2], y)
            bounds[3] = max(bounds[3], y)
    
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        bounds = [x, x, y, y]
        self.sink(image, x, y, bounds)
        return (bounds[1] - bounds[0] + 1) * (bounds[3] - bounds[2] + 1)