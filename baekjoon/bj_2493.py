import sys

N = int(input())
tower = list(map(int, sys.stdin.readline().split()))
stk = []
result = []
for i in range(N):
    while stk:
        if stk[-1][1] > tower[i]:
            result.append(stk[-1][0] + 1)
            break
        stk.pop()

    if not stk:
        result.append(0)

    stk.append([i, tower[i]])

for i in range(N):
    print(result[i], end=' ')