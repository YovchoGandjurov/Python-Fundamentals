import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

data1 = input().split()
data2 = input().split()

point1 = Point(int(data1[0]), int(data1[1]))
point2 = Point(int(data2[0]), int(data2[1]))

side_a = abs(point1.x - point2.x)
side_b = abs(point1.y - point2.y)

distance = math.sqrt(side_a ** 2 + side_b ** 2)
print("{:.3f}".format(distance))
