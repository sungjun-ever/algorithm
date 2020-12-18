# 열, 행, 대각선 경우 다 포함

pos = [0] * 8  # 각 열에서 퀸의 위치를 출력, pos[index] = x 일 때, index는 현재 열, x는 행
flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크
flag_a = [False] * 15   # ↗  대각선 방향 체크
flag_b = [False] * 15   # ↖  대각선 방향 체크


def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력

    for i in range(8):
        for j in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        if (    not flag[j]     # j행에 퀸이 없을 때
                and not flag_a[i+j]  # 대각선 방향으로 퀸이 없을 때
                and not flag_b[i-j+7]):  # 대각선 방향으로 퀸이 없을 때
            pos[i] = j  # 퀸을 j행에 배치
            if i == 7:
                put()  # 모든 열에 퀸 배치를 끝내고 출력
            else:
                flag[j] = flag_a[i+j] = flag_b[i-j+7] = True
                set(i + 1)  # 다음 열에 퀸 배치
                flag[j] = flag_a[i+j] = flag_b[i-j+7] = False


set(0)  # 0 열에 퀸을 배치 시작