import sys

def result(p, lst):
    l, r = 0, len(lst)
    reverse = False
    if r < p.count('D'):
        return 'error'
    for i in p:
        if i == 'R':
            reverse = not reverse
        elif i == 'D':
            if reverse: r -= 1
            else: l += 1

    if len(lst) == 0:
        return '[]'
    else:
        lst = lst[l:r]
        if reverse:
            return '[' + ','.join(reversed(lst)) + ']'
        else:
            return '[' + ','.join(lst) + ']'

T = int(input())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    lst = sys.stdin.readline().strip('[]\n').split(',')
    if n == 0:
        lst = []
    x = result(p, lst)
    print(x)