def qsort(a, left, right) -> None:
    pl = left
    pr = right
    pc = a[(left + right) // 2]

    while pl <= pr: # pl의 인덱스가 더 커지면 종료
        while a[pl] < pc: pl += 1
        while a[pr] > pc: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)


print('퀵 정렬')

num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

qsort(x, 0, len(x)-1)

print('오름차순 퀵 정렬')
print(''.join(str(x)))


