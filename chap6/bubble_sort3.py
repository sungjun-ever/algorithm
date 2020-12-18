def bubble_sort(a) -> None:
    n = len(a)
    l = 0
    while l < n - 1:
        print('사이클')
        last = n - 1
        for j in range(n - 1, l, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
                print(''.join(str(a)))
        l = last

print('버블 정렬')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print('정렬 전')
print(''.join(str(x)))
print('\n정렬 후')
bubble_sort(x)