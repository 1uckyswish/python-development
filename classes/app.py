class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"POINT {self.x}, {self.y}")


point = Point(3,4)
point2 = Point(4,5)
point.draw()
point2.draw()
print(point2)


