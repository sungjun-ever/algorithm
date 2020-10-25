from typing import Any, Sequence
import copy

def line_search(x:Sequence, key:Any) -> int:
    a = copy.deepcopy(x)  # x를 복사해 배열 a를 만들어줍니다.
    a.append(key)   # a 끝에 key 값을 넣어줍니다.

    for i in range(len(a)):
        if a[i] == key:
            break
    return -1 if i == len(x) else i
    # i 값이 x의 크기와 같으면 보초로 넣어준 key을 찾은 것이기 때문에 -1 리턴


print('-----보초법-----')

num = int(input('원소의 수를 입력하세요.: '))

x = [None] * num    # 원소 수가 num인 배열을 만들어준다.

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

ky = int(input('검색할 원소의 값을 입력해주세요.: '))

result = line_search(x, ky)

if result == -1:
    print('검색한 원소의 값이 없습니다.')
else:
    print(f'검색한 원소는 x[{result}]에 있습니다.')