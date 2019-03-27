import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def CalculateDistance(self, second_point):
        side_a = abs(self.x - second_point.x)
        side_b = abs(self.y - second_point.y)
        distance = math.sqrt(side_a ** 2 + side_b ** 2)
        return distance


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.width = Point.CalculateDistance(self.upper_left,
                                             self.upper_right)
        self.height = Point.CalculateDistance(self.upper_left,
                                              self.bottom_left)

    @property
    def CalculatePerimeter(self):
        return (2 * self.width) + (2 * self.height)

    @property
    def CalculateArea(self):
        return self.width * self.height


data = input()
list_box = []

while data != "end":
    result = data.split(" | ")
    top_left = Point(int(result[0].split(":")[0]),
                     int(result[0].split(":")[1]))
    top_right = Point(int(result[1].split(":")[0]),
                      int(result[1].split(":")[1]))
    bot_left = Point(int(result[2].split(":")[0]),
                     int(result[2].split(":")[1]))
    bot_right = Point(int(result[2].split(":")[0]),
                      int(result[2].split(":")[1]))

    box = Box(top_left, top_right, bot_left, bot_right)
    list_box.append(box)

    data = input()

for item in list_box:
    print(f"Box: {int(item.width)}, {int(item.height)}")
    print(f"Perimeter: {int(item.CalculatePerimeter)}")
    print(f"Area: {int(item.CalculateArea)}")
