from typing import Any, Sequence


def line_search(x: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(x):
            return -1
        if x[i] == key:
            return i
        i += 1
    # 검색한 원소의 값이 있으면 인덱스 값 i 리턴, i가 x의 크기와 같으면 -1 리턴


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