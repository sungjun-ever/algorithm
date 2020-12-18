import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
lst = [None] * N
ans = []
for i in range(N):
    lst[i] = sys.stdin.readline().rstrip()

lst.sort()

for _ in range(M):
    key = sys.stdin.readline().rstrip()
    pl = 0
    pr = N-1
    while True:
        pc = (pl + pr) // 2
        if lst[pc] == key:
            ans.append(key)
            break
        elif lst[pc] < key:
            pl = pc + 1
        elif lst[pc] > key:
            pr = pc - 1

        if pl > pr:
            break
print(len(ans))
ans.sort()
print('\n'.join(ans))
