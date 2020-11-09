import sys

class Stack:
    def __init__(self):     # 초기화
        self.stk = []

    def size(self):     # 스택의 사이즈
        return len(self.stk)

    def is_empty(self):     # 스택이 비었는지 검사
        return self.size() <= 0

    def push(self, value):      # 스택에 데이터를 넣음
        self.stk.append(value)

    def pop(self):      # 스택에서 데이터를 뺌
        if self.is_empty():
            return -1
        return self.stk.pop()

    def peek(self):     # 스택의 가장 윗 값을 리턴
        if self.is_empty():
            return -1
        return self.stk[-1]


N = int(sys.stdin.readline().strip())
for _ in range(N):
    s = Stack()     # 스택 초기화
    temp = list(input())    # 괄호 문자열 입력받고 리스트로 저장
    for i in temp:
        if s.size() == 0:
            if i == '(':    # 스택이 비어있을 때 i가 '('면 넣어주고
                s.push(i)
            else:
                s.push(i)   # ')'면 규칙에 어긋나기 때문에 for문을 중지시킵니다.
                break
        else:   # 스택에 하나라도 있을 때 가장 윗 값을 비교합니다.
            if s.peek() != i:   # 가장 윗값은 항상 '('이고 i가 ')'이면 팝해줍니다.
                s.pop()

            else:   # i가 '('이면 넣어줍니다.
                s.push(i)

    if s.size() == 0:   # 스택이 비어있다면 괄호가 다 쌍을 이룬 것입니다.
        print('YES')
    else:
        print('NO')
