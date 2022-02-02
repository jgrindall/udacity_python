class Point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
        
    def __add__(self, pt):
        _x = pt.x
        _y = pt.y
        return Point(self._x + _x, self._y + _y)
        
        
    def __str__(self):
        return "point (" + str(self._x) + "," + str(self._y) + ")"
origin = Point()
point = Point(4, 1)
other_point = Point(3, -3)
third_point = point + other_point

print(point)
print(other_point)
print(third_point)