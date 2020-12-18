import sys

N = list(map(int, sys.stdin.readline().rstrip().split()))
N.sort()
for i in N:
    print(i, end=' ')