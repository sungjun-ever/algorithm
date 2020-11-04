from typing import Any

class Stack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def is_empty(self):
        return self.ptr < 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value) -> Any:
        if self.is_full():
            raise Stack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise Stack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        return self.stk[self.ptr - 1]


n = int(input())
s = Stack(n)
x = []
for i in range(n):
    num = int(input())
    x.append(num)

index = 0
stkNum = 1
temp = []
while index <= n - 1:
    if s.peek() == x[index]:
        try:
            pop = s.pop()
            index += 1
            temp.append('-')
        except Stack.Empty:
            temp.append('None')
            break
    else:
        try:
            s.push(stkNum)
            stkNum += 1
            temp.append('+')
        except Stack.Full:
            temp.append('None')
            break

if 'None' in temp:
    print('NO')
else:
    for t in range(len(temp)):
        print(temp[t])