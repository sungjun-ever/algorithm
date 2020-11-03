from typing import Any

class FixedStack:
    #고정 길이 스택 클래스

    class Empty(Exception):
        #비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        # 가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리
        pass

    def __init__(self, capacity: int = 256) -> None:
        # 스택 초기화
        self.stk = [None] * capacity    # 스택 배열
        self.capacity = capacity    # 스택의 크기
        self.ptr = 0    # 스택 포인터
        
    def __len__(self) -> int:
        # 스택에 쌓여 있는 데이터 개수를 반환
        return self.ptr

    def is_empty(self) -> bool:
        # 스택이 비어있는지 판단
        return self.ptr <= 0

    def is_full(self) -> bool:
        # 스택이 가득 차 있는지 판단
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        # 스택에 데이터를 푸시
        if self.is_full():
            raise FixedStack.Full   # 스택이 가득차 있는지 확인
        self.stk[self.ptr] = value  # 현재 포인터에 데이터를 넣어주고
        self.ptr += 1   # 포인터에 + 1

    def pop(self) -> Any:
        # 스택에서 데이터를 팝(꺼내옴)
        if self.is_empty():
            raise FixedStack.Empty  # 스택이 비어 있는지 확인
        self.ptr -= 1   # 데이터의 개수를 뜻하므로 -1한 값이 최종 인덱스 값과 같습니다.
        return self.stk[self.ptr]   # 가장 위에 데이터를 리턴
    
    def peek(self) -> Any:
        # 스택 꼭대기에 있는 데이터를 리턴
        if self.is_empty():
            raise FixedStack.Empty  # 스택이 비어 있는지 확인
        return self.stk[self.ptr - 1] # 가장 위에 데이터를 리턴

    def clear(self) -> None:
        # 스택을 비움
        self.ptr = 0

    def find(self, value: Any) -> Any:
        # 스택에서 데이터를 찾아 인덱스를 반환
        for i in range(self.ptr - 1, -1, -1):   # 탑부터 데이터를 찾습니다.
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        # 스택에 있는 데이터의 개수를 반환
        c = 0
        for i in range(self.ptr):   
            if self.stk[i] == value:
                c += 1
        return c    # 스택에서 해당 데이터를 찾아 데이터의 개수를 리턴합니다.
    
    def __contains__(self, value: Any) -> bool:
        # 스택에 데이터가 있는지 판단
        return self.count(value)

    def dump(self) -> None:
        # 스택 안의 데이터를 바텀부터 탑 순서로 출력
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])