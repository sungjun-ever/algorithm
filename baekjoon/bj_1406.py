import sys

stk = list(sys.stdin.readline().strip())

M = int(input())
temp_stk = []
for _ in range(M):
    menu = sys.stdin.readline().strip().split()
    if menu[0] == 'L':
        if stk:
            temp_stk.append(stk.pop())

    elif menu[0] == 'D':
        if temp_stk:
            stk.append(temp_stk.pop())

    elif menu[0] == 'B':
        if stk:
            stk.pop()

    elif menu[0] == 'P':
        stk.append(menu[1])

print(''.join(stk + list(reversed(temp_stk))))

