from enum import Enum
from class_test import ChainHash

Menu = Enum('Menu', ['add', 'remove','search', 'printed', 'exit'])
# 메뉴를 만들어줍니다.

def select_menu() -> Menu:  # 메뉴를 선택합니다.
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = input('추가할 키를 입력하세요.:')
        value = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, value):
            print('추가 실패')
        else:
            print('추가 성공')

    elif menu == Menu.remove:
        key = input('삭제할 키를 입력하세요.:')
        if not hash.remove(key):
            print('삭제를 실패했습니다.')
        else:
            print('삭제 성공')

    elif menu == Menu.search:
        key = input('검색할 키를 입력하세요.:')
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색에 실패 했습니다.')

    elif menu == Menu.printed:
        hash.printed()

    else:
        break