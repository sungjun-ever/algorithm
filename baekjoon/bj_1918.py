import sys

def priority(v):
    if v == '*' or v == '/':
        return 3
    elif v == '+' or v == '-':
        return 2
    elif v == '(':
        return 1

stk = []
result = ''
x = sys.stdin.readline().rstrip()
for i in '(' + x + ')':
    if 'A' <= i <= 'Z':
        result += i
    elif i == '(':
        stk.append(i)
    elif i == ')':
        while True:
            ps = stk.pop()
            if ps == '(':
                break
            result += ps
    else:
        while stk[-1] != '(' and priority(i) <= priority(stk[-1]):
            result += stk.pop()
        stk.append(i)

print(result)


