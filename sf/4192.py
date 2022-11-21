from collections import deque

def bfs(sty, stx, dey, dex):
    q = deque()
    q.append((sty, stx, 0))
    visited[sty][stx] = True

    while q:
        cy, cx, ct = q.popleft()
        if cy == dey and cx == dex:
            return ct
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and pool[ny][nx] == 0:
                q.append((ny, nx, ct + 1))
                visited[ny][nx] = True

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