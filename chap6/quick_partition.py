def partition(a) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    pc = a[n//2]

    while pl <= pr: # pl의 인덱스가 더 커지면 종료
        while a[pl] < pc: pl += 1
        while a[pr] > pc: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'기준은 {pc}입니다.')

    print(f'기준 이하의 그룹: {a[0 : pl]}')

    print(f'기준 이상의 그룹: {a[pr + 1 : n]}')


print('배열을 두 그룹으로 나누기')

num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

partition(x)

