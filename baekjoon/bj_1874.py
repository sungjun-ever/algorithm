from typing import Any

class Stack:
    def __init__(self, capacity: int) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, value) -> Any:
        # if self.is_full():
        #     raise Stack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        # if self.is_empty():
        #     raise Stack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        return self.stk[self.ptr - 1]


n = int(input())
s = Stack(n)
stkNum = 1
temp = []

for i in range(n):
    num = int(input())
    while stkNum <= num:
        s.push(stkNum)
        stkNum += 1
        temp.append('+')
    if s.peek() == num:
        s.pop()
        temp.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(temp))