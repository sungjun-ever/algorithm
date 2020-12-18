def gcd(x: int, y: int) -> int:
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    x = int(input('첫 번째 정수값을 입력하세요.: '))
    y = int(input('두 번째 정수값을 입력하세요.: '))

    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')
