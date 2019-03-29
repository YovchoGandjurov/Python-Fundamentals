import re


class Fish:
    def __init__(self, fish_vision, tail, body, head):
        self.fish_vision = fish_vision
        self.tail = len(tail)
        self.body = len(body)
        self.head = head

        self.tail_len = self.tail * 2
        self.body_len = self.body * 2

    @property
    def tail_type(self):
        status = "None"
        if self.tail > 5:
            status = "Long ({} cm)".format(self.tail_len)
        elif self.tail > 1:
            status = "Medium ({} cm)".format(self.tail_len)
        elif self.tail == 1:
            status = "Short ({} cm)".format(self.tail_len)
        return status

    @property
    def body_type(self):
        status = "None"
        if self.body > 10:
            status = "Long ({} cm)".format(self.body_len)
        elif self.body > 5:
            status = "Medium ({} cm)".format(self.body_len)
        elif self.body <= 5:
            status = "Short ({} cm)".format(self.body_len)
        return status

    @property
    def status(self):
        status = None
        if self.head == "'":
            status = "Awake"
        elif self.head == "-":
            status = "Asleep"
        elif self.head == "x":
            status = "Dead"
        return status

data = input()
pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<head>[-x'])>"
matches = re.finditer(pattern, data)
fishes = []
match_list = [x for x in matches]

if len(match_list) == 0:
    print("No fish found.")

for fish in match_list:
    fish_vision = fish.group()
    tail = fish.group("tail")
    body = fish.group("body")
    head = fish.group("head")
    curr_fish = Fish(fish_vision, tail, body, head)
    fishes.append(curr_fish)


for item in fishes:
    print("Fish {}: {}".format(fishes.index(item) + 1, item.fish_vision))
    print("  Tail type: {}".format(item.tail_type))
    print("  Body type: {}".format(item.body_type))
    print("  Status: {}".format(item.status))
