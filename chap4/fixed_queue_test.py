from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['enque', 'deque', 'peek', 'find', 'dump', 'exit'])


def select_menu():
    string = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*string, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)

while True:
    print('ㅡ' * 20)
    print(f'현재 데이터의 개수: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.enque:
        value = int(input('넣을 데이터를 입력하세요.: '))
        try:
            q.enque(value)
        except FixedQueue.Full:
            print('큐가 가득 차있습니다.')

    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'꺼낸 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어있습니다.')

    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f'가장 앞 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어있습니다.')

    elif menu == Menu.find:
        value = int(input('검색할 데이터를 입력하세요.: '))
        if value in q:
            print(f'{q.count(value)}개 있고, 맨 앞 위치는 {q.find(value)}입니다.')
        else:
            print('검색값이 없습니다.')

    elif menu == Menu.dump:
        q.dump()

    else:
        break