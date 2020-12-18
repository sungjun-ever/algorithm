def shell_sort(a):
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            print(f'그룹 인덱스: {j}, {h}')
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
            print(f'정렬 결과 {a}')
        h = h // 3

print('셸 정렬')
num = int(input('원소 소 입력: '))
x = [None] * num
for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

shell_sort(x)