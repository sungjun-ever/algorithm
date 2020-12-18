import sys

class Stack:

    def __init__(self):
        self.stk = []

    def append(self, value):
        self.stk.append(value)

    def pop(self):
        return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            return -1
        return self.stk[-1]

    def size(self):
        return len(self.stk)

while True:
    ss = Stack()
    cnt = 0
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    for i in string:
        if i == '(' or i == '[':
            ss.append(i)

        elif i == ']':
            if ss.peek() == '[':
                ss.pop()
            else:
                cnt += 1

        elif i == ')':
            if ss.peek() == '(':
                ss.pop()
            else:
                cnt += 1

    if ss.size() == 0 and cnt == 0:
        print('yes')
    else:
        print('no')
