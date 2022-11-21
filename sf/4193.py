from collections import deque

def bfs(sty, stx, dey, dex):
    q = deque()
    q.append((sty, stx, 0))
    visited[sty][stx] = True

    while q:
        for _ in range(len(q)):
            cy, cx, ct = q.popleft()
            if cy == dey and cx == dex:
                return ct

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if not(0 <= ny < N) or not(0 <= nx < N) or visited[ny][nx] or pool[ny][nx] == 1:
                    continue

                if pool[ny][nx] == 2:
                    if ct % 3 != 2: # 소용돌이가 존재하는 경우 -> 다음 시간대에 확인
                        q.append((cy, cx, ct + 1))
                        continue

                q.append((ny, nx, ct + 1))
                visited[ny][nx] = True
    return -1

T = int(input())

for tc in range(T):
    N = int(input())
    pool = [list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(N)]

    print("#{} {}".format(tc + 1, bfs(A, B, C, D)))