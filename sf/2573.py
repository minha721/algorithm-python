from collections import deque

def melt():
    temp = []

    for i in range(N):
        t = []
        for j in range(M):
            cnt = 0
            if graph[i][j] > 0:
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < M:
                        if graph[i + dx[k]][j + dy[k]] == 0:
                            cnt += 1
                if graph[i][j] - cnt >= 0:
                    t.append(graph[i][j] - cnt)
                else:
                    t.append(0)
            else:
                t.append(0)
        temp.append(t)

    return temp

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] >= 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while True:
    visited = [[False] * M for _ in range(N)]

    graph = melt()
    year += 1

    land = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 1 and not visited[i][j]:
                visited[i][j] = True
                land += bfs(i, j)

    if land == 0:
        print(0)
        break
    elif land > 1:
        print(year)
        break