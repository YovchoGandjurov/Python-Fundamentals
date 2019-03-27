class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height


def is_inside(rec1, rec2):
    if rec1.left >= rec2.left and rec1.right <= rec2.right and \
                    rec1.top <= rec2.top and rec1.bottom <= rec2.bottom:
        print("Inside")
    else:
        print("Not inside")

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

r1 = Rectangle(data1[0], data1[1], data1[2], data1[3])
r2 = Rectangle(data2[0], data2[1], data2[2], data2[3])

is_inside(r1, r2)
