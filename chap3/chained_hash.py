from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next):
        # 초기화
        self.key = key  # 키
        self.value = value  # 값
        self.next = next  # 다음 노드를 참조


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        # 초기화
        self.capacity = capacity  # 해시 리스트의 크기 지정
        self.table = [None] * capacity  # 해시 리스트를 선언

    def hash_value(self, key: Any) -> int:
        # 해시 값을 구함
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is not None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next
            print()