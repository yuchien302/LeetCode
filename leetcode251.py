class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.r, self.c = 0, 0
        self.vec2d = vec2d
        while self.r < len(vec2d) and len(vec2d[self.r]) == 0:
            self.r += 1
        if self.r == len(vec2d):
            self.r = -1


    def next(self):
        """
        :rtype: int
        """
        val = self.vec2d[self.r][self.c]
        self.c += 1
        if self.c == len(self.vec2d[self.r]):
            self.c = 0
            self.r += 1

        while self.r < len(self.vec2d) and self.c == len(self.vec2d[self.r]) == 0:
            self.r += 1

        if self.r == len(self.vec2d):
            self.r = -1

        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.r != -1


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())