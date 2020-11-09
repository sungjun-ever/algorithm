from typing import Any
from _collections import deque

class Stack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, maxlen: int = 256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        if self.is_full():
            raise Stack.Full
        self.__stk.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise Stack.Empty
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> int:
        print(list(self.__stk))