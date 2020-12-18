def bubble_sort(a) -> None:
    left = 0
    right = len(a) - 1
    last = right
    n = len(a)
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        print('작은 수')
        print(''.join(str(a)))

        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last
        print('큰 수')
        print(''.join(str(a)))

print('버블 정렬')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print('정렬 전')
print(''.join(str(x)))
print('\n정렬 후')
bubble_sort(x)