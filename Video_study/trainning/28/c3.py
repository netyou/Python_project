import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x ** 2 + self.y** 2)

    def get_len(self):
        return self.len


# 其他类中的方法可以先行在类中使用
p1 = Point(2, 3)
p2 = Point(5, 7)
line = Line(p1, p2)
print(line.get_len())
