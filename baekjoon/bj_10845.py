from typing import Any
import sys
from collections import deque

class Queue:
    def __init__(self) -> None:
        self.que = deque([], None)

    def is_empty(self):
        if len(self.que) <= 0:
            return 1
        return 0

    def push(self, value):
        self.que.append(value)

    def pop(self) -> Any:
        if len(self.que) <= 0:
            return -1
        x = self.que.popleft()
        return x

    def size(self) -> Any:
        return len(self.que)

    def front(self) -> Any:
        if len(self.que) <= 0:
            return -1
        return self.que[0]

    def back(self) -> Any:
        if len(self.que) <= 0:
            return -1
        return self.que[-1]



N = int(input())
n = 0
q = Queue()
while n < N:
    n += 1
    menu = sys.stdin.readline().rstrip().split()

    if menu[0] == 'push':
        q.push(menu[1])

    elif menu[0] == 'pop':
        print(q.pop())

    elif menu[0] == 'size':
        print(q.size())

    elif menu[0] == 'empty':
        print(q.is_empty())

    elif menu[0] == 'front':
        print(q.front())

    elif menu[0] == 'back':
        print(q.back())




