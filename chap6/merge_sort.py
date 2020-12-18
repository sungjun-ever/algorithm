def merge_sort(a) -> None:

    def sub_merge_sort(a, left, right) -> None:
        if left < right:
            center = (left + right) // 2

            sub_merge_sort(a, left, center)     # 배열의 앞 부분
            sub_merge_sort(a, center+1, right)  # 배열의 뒷 부분

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    sub_merge_sort(a, 0, n-1)
    del buff


print('병합 정렬')
num = int(input('원소 수 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

merge_sort(x)

print('오름차순 정렬')
