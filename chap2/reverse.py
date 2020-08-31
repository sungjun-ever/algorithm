from typing import MutableSequence, Any

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    
if __name__ == '__main__':
    print('배열의 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.'))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]의 원소를 입력하세요.: '))

    print(f'정렬 전 배열 {x}')
    reverse_array(x)

    print('배열의 원소를 역순으로 정렬했습니다.')
    print(f'정렬 후 배열 {x}')