from chap4.fixed_stack import FixedStack

def qsort(a, left: int, right: int) -> None:
    range = FixedStack(right - left + 1)

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = a[(left + right) // 2]  # 가운데 원소

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))
        if pl < right: range.push((pl, right))


print('퀵 정렬(비재귀)')
num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

qsort(x, 0, len(x)-1)

print('오름차순 퀵 정렬')
print(''.join(str(x)))
