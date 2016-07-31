class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i1 = 0 # outer level index
        self.i2 = 0 # inner level index

        self._moveToValid()

    def _moveToValid(self):
        """
        move i1 and i2 to a valid position, so that self.vec2d[self.i1][self.i2] is valid
        """
        while self.i1 < len(self.vec2d) and self.i2 >= len(self.vec2d[self.i1]):
            self.i1 += 1
            self.i2 = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.i1][self.i2]
        self.i2 += 1
        self._moveToValid()

        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.vec2d)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())