import heapq


def merge_sort(a) -> None:

    def sub_merge_sort(a, left, right) -> None:
        if left < right:
            center = (left + right) // 2

            sub_merge_sort(a, left, center)            # 앞부분 배열의 병합 정렬
            sub_merge_sort(a, center + 1, right)       # 뒷부분 배열의 병합 정렬

            buff = list(heapq.merge(a[left: center+1], a[center + 1: right+1]))

            for i in range(len(buff)):
                a[left + i] = buff[i]

    sub_merge_sort(a, 0, len(a)-1)       # 배열 전체를 병합 정렬


print('병합 정렬(heapq.merge를 사용).')
num = int(input('원소 수를 입력: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

merge_sort(x)

print('오름차순으로 정렬했습니다.')
print(''.join(str(x)))