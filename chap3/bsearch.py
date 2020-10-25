from typing import Any, Sequence

def search_tree(x: Sequence, key: Any):
    pl = 0
    pr = len(x) - 1

    while True:
        pc = (pl + pr) // 2
        if x[pc] == key:
            return pc
        elif x[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    return -1

print('이진검색\n')

num = int(input('원소 수를 입력하세요.: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

ky = int(input('검색할 숫자를 입력하세요.: '))

result = search_tree(x, ky)

if result == -1:
    print('검색값을 가지는 원소가 없습니다.')
else:
    print(f'검색 원소는 x[{result}]에 있습니다.')





