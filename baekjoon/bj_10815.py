import sys

def com(a, b):
    for i in range(len(b)):
        key = b[i]
        pl = 0
        pr = len(a) - 1
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                print(1, end=' ')
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl > pr:
                print(0, end=' ')
                break


N = int(input())
num = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
ex = list(map(int, sys.stdin.readline().rstrip().split()))

num.sort()
com(num, ex)
