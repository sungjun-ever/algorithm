from typing import Any, Sequence


def line_search(x: Sequence, key: Any) -> int:
    for i in range(len(x)):
        if x[i] == key:
            return i
    return -1



print('-----선형검색-----')

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