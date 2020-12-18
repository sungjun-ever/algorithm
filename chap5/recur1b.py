def recur(n: int) -> int:
    stk = []
    while True:
        if n > 0:
            stk.append(n)
            n = n - 1
            continue
        if stk:
            n = stk.pop()
            print(n)
            n = n - 2
            continue
        break


x = int(input('정숫값을 입력하세요.: '))
recur(x)