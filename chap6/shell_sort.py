def shell_sort(a):
    n = len(a)
    h = n // 2  # 4-정렬, 2-정렬 >> h-정렬
    while h > 0:
        for i in range(h, n):
            j = i - h
            print(f'그룹 인덱스: {j}, {i}')
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
            print(f'정렬 결과 {a}')
        h = h // 2
        print()

print('셸 정렬')
num = int(input('원소 소 입력: '))
x = [None] * num
for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

shell_sort(x)