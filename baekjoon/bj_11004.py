import sys

N, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
print(lst[k-1])
