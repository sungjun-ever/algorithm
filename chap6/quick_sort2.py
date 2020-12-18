def sort3(a, idx1, idx2, idx3):
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a ,left, right):
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp


def qsort(a, left, right):
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl+pr)//2, pr)    # 중앙값
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]   # 중앙값과 끝에서 두 번째 원소 바꿔줌
        pl += 1
        pr -= 2     # 정렬 범위 축소

        while pl <= pr:
            while a[pl] < x : pl += 1
            while a[pr] > x : pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)


print('퀵 정렬(원소가 9개 미만일 경우 단순 삽입 정렬)')
num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

qsort(x, 0, len(x)-1)

print('오름차순 정렬')

print(''.join(str(x)))