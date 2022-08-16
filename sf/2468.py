from collections import deque

def bfs(x, y, v, visited):
    q = deque([(x, y)])

    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if city[nx][ny] > v and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
maxVol = max(sum(city, []))
res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for v in range(0, maxVol + 1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if city[i][j] > v and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                bfs(i, j, v, visited)

    res.append(cnt)

print(max(res))