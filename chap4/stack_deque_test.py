from enum import Enum
from stack_deque import Stack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'find', 'dump', 'exit'])


def select_menu():
    s = [f'({m.value}){m.name}' for m in Menu]
    print(*s, sep= '  ')
    n = int(input('메뉴를 선택하세요.: '))
    if 1 <= n <= len(Menu):
        return Menu(n)

s = Stack(16)

while True:
    print(f'스택의 상태: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        try:
            x = int(input('추가 할 값을 입력하세요.: '))
            s.push(x)
            print('추가 완료\n')
        except Stack.Full:
            print('스택에 자리가 없습니다.\n')

    elif menu == Menu.pop:
        try:
            pop = s.pop()
            print(f'팝한 값은 {pop}입니다.\n')
        except Stack.Empty:
            print('스택이 비어있습니다.\n')

    elif menu == Menu.peek:
        print(f'가장 위에 값은 {s.peek()}입니다.\n')

    elif menu == Menu.find:
        x = int(input('찾을 값을 입력하세요.: '))
        find = s.find(x)
        if find == -1:
            print('찾는 값이 스택 안에 없습니다.\n')
        else:
            print(f'{x}는 {find} 위치에 있습니다.\n')

    elif menu == Menu.dump:
        s.dump()
        print('\n')

    else:
        break

