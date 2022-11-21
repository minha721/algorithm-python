dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# k의 최대 사이즈 300
mSize = 300

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    init_cell = [list(map(int, input().split())) for _ in range(N)]

    # 세로 (mSize * 2 + n), 가로 (mSize * 2 + m) 으로 설정
    vessel = [[0] * (mSize * 2 + M) for _ in range(mSize * 2 + N)]

    cell = {}

    for i in range(N):
        for j in range(M):
            if init_cell[i][j] > 0:
                vessel[mSize // 2 + i][mSize // 2 + j] = init_cell[i][j]
                cell[(mSize // 2 + i, mSize // 2 + j)] = [-1, 0, init_cell[i][j]]

    for _ in range(K):
        keys = list(cell.keys())

        for y, x in keys:
            # 활성 상태, 상태 진행 시간, 생명력 수치
            state, time, live = cell[(y, x)]

            # 상태 진행 시간 1 증가
            cell[(y, x)][1] += 1

            # 활성화 -> 비활성 상태이고 생명력 수치만큼 시간이 지났을 때
            # 활성 상태 1로 바꿔주고, 상태 진행 시간 0으로 바꿔줌(상태 변했으니까)
            if cell[(y, x)][0] == -1 and cell[(y, x)][1] == live:
                cell[(y, x)][0] = 1
                cell[(y, x)][1] = 0

            # 세포 분열 -> 활성 상태이고 1만큼 진행했을 때
            if cell[(y, x)][0] == 1 and cell[(y, x)][1] == 1:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    # 탐색 칸이 0이고
                    if vessel[ny][nx] == 0:
                        # 아무것도 없는 칸이라면 -> 분열
                        if cell.get((ny, nx)) is None:
                            vessel[ny][nx] = live
                            cell[(ny, nx)] = [-1, 0, live]
                        # 이번 타임에 다른 세포가 번식했다면 -> 비교해서 내가 더 크면 갱신
                        elif cell[(ny, nx)][0] == -1 and cell[(ny, nx)][1] == 0:
                            if vessel[ny][nx] < live:
                                vessel[ny][nx] = live
                                cell[(ny, nx)] = [-1, 0, live]

            # 세포 죽음 -> 활성 상태이고, live만큼 진행했을 때
            if cell[(y, x)][0] == 1 and cell[(y, x)][1] == live:
                cell.pop((y, x))

    print("#{} {}".format(tc + 1, len(cell)))