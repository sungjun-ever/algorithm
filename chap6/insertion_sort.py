def insertion_sort(a) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp


print('단순 삽입 정렬')
num = int(input('원소 수 입력: '))
x = [None] * num    # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

print(''.join(str(x)))
insertion_sort(x)
print(''.join(str(x)))