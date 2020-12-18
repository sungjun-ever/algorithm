N = input()
lst = list(map(int, N))
total = sum(lst)

if total % 3 == 0:
    lst.sort(reverse=True)
    if lst[-1] == 0:
        print(''.join(map(str, lst)))
    else:
        print(-1)
else:
    print(-1)