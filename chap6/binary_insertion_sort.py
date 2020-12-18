import bisect
def binary_insertion_sort(a):
    '''
        for i in range(1, len(a)):
            bisect.insort(a, a.pop(i), 0, i)
    '''
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        if pl <= pr:
            pd = pc + 1
        else:
            pd = pr + 1
        print(f'pl: {pl}, pr: {pr}, pd: {pd}')
        for j in range(i, pd, -1):
            a[j] = a[j-1]

        a[pd] = key
        print(a)


print('이진 삽입 정렬')
num = int(input('원소 수 입력: '))
x = [None] * num    # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print(''.join(str(x)))
binary_insertion_sort(x)
print(''.join(str(x)))