def triagle_top(num):
    for i in range(1, num+1):
        for x in range(1, i+1):
            print(x, end=' ')
        print()


def triagle_bot(num):
    for i in range(num, 1, -1):
        for x in range(1, i):
            print(x, end=' ')
        print()

n = int(input())
triagle_top(n)
triagle_bot(n)
