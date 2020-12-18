import sys

def set(start, index):
    if index == 6:
        for i in range(6):
            print(f'{temp[i]}', end=' ')
        print()
    for i in range(start, len(lst)):
        temp[index] = lst[i]
        set(i+1, index+1)


temp = [0] * 13
while True:
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    if lst[0] == 0:
        break
    del lst[0]
    set(0, 0)
    print()
