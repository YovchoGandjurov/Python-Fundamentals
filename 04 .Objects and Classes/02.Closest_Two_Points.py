import math
import itertools


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


number_points = int(input())
points = []

for index in range(number_points):
    data = input().split()
    points.append(Point(int(data[0]), int(data[1])))


def find_closest_points(points):
    closest_points = []
    distance = 0

    for item, next_item in itertools.combinations(points, 2):
        side_a = abs(item.x - next_item.x)
        side_b = abs(item.y - next_item.y)
        curr_distance = math.sqrt(side_a ** 2 + side_b ** 2)

        if distance == 0 or curr_distance < distance:
            closest_points = []
            closest_points.extend([item, next_item])
            distance = curr_distance

    closest_points.append(distance)
    return closest_points


print(f"{find_closest_points(points)[-1]:.3f}")
print("({}, {})".format(find_closest_points(points)[0].x,
                        find_closest_points(points)[0].y))
print("({}, {})".format(find_closest_points(points)[1].x,
                        find_closest_points(points)[1].y))
