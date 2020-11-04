import sys

class Stack:
    def __init__(self):
        self.stk = [None] * 10000
        self.ptr = 0

    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        if self.ptr < 0:
            self.ptr = 0
            return -1
        return self.stk[self.ptr]

    def size(self):
        return self.ptr

    def empty(self):
        if self.ptr <= 0:
            return 1
        return 0

    def top(self):
        if self.ptr <= 0:
            return -1
        return self.stk[self.ptr - 1]


N = int(input())
s = Stack()

for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    menu = cmd[0]

    if menu == 'push':
        s.push(cmd[1])

    elif menu == 'pop':
        print(s.pop())

    elif menu == 'size':
        print(s.size())

    elif menu == 'empty':
        print(s.empty())

    elif menu == 'top':
        print(s.top())
