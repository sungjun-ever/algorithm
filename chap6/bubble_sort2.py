def bubble_sort(a) -> None:
    n = len(a)
    for i in range(n - 1):
        print(f'사이클 {i}')
        exchange = 0
        for j in range(n - 1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange += 1
        if exchange == 0:
            break
        print(''.join(str(x)))

print('버블 정렬')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print('정렬 전')
print(''.join(str(x)))
print('\n정렬 후')
bubble_sort(x)