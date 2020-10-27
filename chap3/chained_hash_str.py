from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key  # 키
        self.value = value  # 값
        self.next = next  # 뒤쪽 노드 참조


class ChainHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity  # 배열의 크기 지정
        self.table = [None] * capacity  # 배열 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity  # 해시 값을 구해줌
        return (int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)   # 입력 값의 해시값 저장
        p = self.table[hash]    # 해당 인덱스 값을 가지는 노드

        while p is not None:
            # 해당 인덱스가 비어있지 않으면 값이 있기 때문에 계속 찾아줍니다.
            if p.key == key:
                return p.value     # 입력 값을 찾으면 해시값을 리턴해줍니다.
            p = p.next  # 다음 노드를 보게합니다.

        return None     # 입력 값을 찾지 못했다면 None 리턴합니다.

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)   # 입력 값의 해시값 저장
        p = self.table[hash]    # 해당 인덱스 값을 가지는 노드

        while p is not None:
            if p.key == key:    # 값을 넣어야 하는데 이미 있으면 안되기 때문에 넣어줍니다.
                return False
            p = p.next  # 다음 노드를 보게합니다.

        temp = Node(key, value, self.table[hash])    # 넣을 값이 배열 안에 없다면 노드로 만들어 주고
        self.table[hash] = temp     # 노드를 추가합니다.
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        bp = None   # 바로 앞의 노드
        while p is not None:
            if p.key == key:    # 삭제할 값을 찾았을 때 실행합니다.
                if bp is None:  
                    self.table[hash] = p.next   
                    # 앞 노드가 None이면table[hash]값을 삭제할 노드의 다음 노드 값을 줍니다.
                else:
                    bp.next = p.next    
                    # 앞 노드가 None이 아니면 앞 노드에 삭제할 노드의 다음 노드 값을 줍니다.
                return True
            bp = p
            p = p.next
            # 값을 찾을 때까지 앞 노드와 현재 노드 값을 한 단계씩? 바꿔줍니다.
        return False

    def printed(self) -> None:      # 원소들이 제대로 된 위치에 들어갔는지 출력해봅니다.
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key}({p.value})', end='')
                p = p.next
            print()
