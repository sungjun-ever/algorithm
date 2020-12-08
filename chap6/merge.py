def merge_sorted_list(a, b, c) -> None:
    pa, pb, pc = 0, 0, 0    # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)     # 각 배열의 크기

    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
            print('\nwhile 1')
            print(f'배열 a: {a[pa:]}')
            print(f'배열 b: {b[pb:]}')
            print(f'배열 c: {c}')
        else:
            c[pc] = b[pb]
            pb += 1
            print('\nwhile 1')
            print(f'배열 a: {a[pa:]}')
            print(f'배열 b: {b[pb:]}')
            print(f'배열 c: {c}')
        pc += 1

    while pa < na:
        print('\nwhile 2')
        print(f'배열 a: {a[pa:]}')
        print(f'배열 c: {c}')
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:
        print('\nwhile 3')
        print(f'배열 b: {b[pb:]}')
        print(f'배열 c: {c}')
        c[pc] = b[pb]
        pb += 1
        pc += 1


a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = [None] * (len(a) + len(b))

merge_sorted_list(a, b, c)

print(f'\n배열 a: {a}')
print(f'배열 b: {b}')
print(f'배열 c: {c}')