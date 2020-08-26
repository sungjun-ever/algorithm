print('1부터 N까지 합구하기.')

n = int(input('n 값을 입력하세요.: '))

sum = 0

for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지의 합은 {sum}입니다.')
