def bubble_sort(lst):
    flag = True
    while flag:
        flag = False

        for x in range(len(lst) - 1):
            next_elem = x + 1
            if lst[x] > lst[next_elem]:
                lst[x], lst[next_elem] = lst[next_elem], lst[x]
                flag = True

n = [int(x) for x in input().split()]
bubble_sort(n)
print(' '.join([str(x) for x in n]))
