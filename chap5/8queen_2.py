# 열 뿐만 아니라, 행에서도 겹치지 않게 추가

pos = [0] * 8  # 각 열에서 퀸의 위치를 출력, pos[index] = x 일 때, index는 현재 열, x는 행
flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크

def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        if not flag[j]:
            pos[i] = j  # 퀸을 j행에 배치
            if i == 7:
                put()  # 모든 열에 퀸 배치를 끝내고 출력
            else:
                flag[j] = True
                set(i + 1)  # 다음 열에 퀸 배치
                flag[j] = False

set(0)  # 0 열에 퀸을 배치 시작