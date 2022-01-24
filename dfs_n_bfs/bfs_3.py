from collections import deque

n, m, k = map(int, input().split())
trash = []

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = []

for i in range(k):
    trash.append(list(map(int, input().split())))

for i, j in trash:
    graph[i - 1][j - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count.append(bfs(i, j))

print(max(count))
