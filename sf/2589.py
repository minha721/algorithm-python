from collections import deque

def bfs(x, y):
    visited = [[False] * width for _ in range(height)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    cnt = []

    while q:
        qx, qy, c = q.popleft()
        cnt.append(c)

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < height and 0 <= ny < width:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    q.append((nx, ny, c + 1))
                    visited[nx][ny] = True

    return max(cnt)

height, width = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(height)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []
for i in range(height):
    for j in range(width):
        if graph[i][j] == 'L':
            res.append(bfs(i, j))

print(max(res))