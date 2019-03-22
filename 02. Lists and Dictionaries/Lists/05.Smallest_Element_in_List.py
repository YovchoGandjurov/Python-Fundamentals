def smallest(lst):
    smallest_int = lst[0]
    for i in lst:
        if i < smallest_int:
            smallest_int = i
    return smallest_int

n = [int(x) for x in input().split(' ')]
print(smallest(n))
