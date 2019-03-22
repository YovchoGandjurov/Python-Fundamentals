def insertion_sort(lst):
    for x in range(1, len(lst)):
        j = x
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

n = [int(x) for x in input().split()]
insertion_sort(n)
print(' '.join([str(x) for x in n]))
