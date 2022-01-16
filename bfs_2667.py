from collections import deque

N = int(input())
graph = []
visited = [[False]*N for _ in range(N)]
house = []
total = 0

for i in range(N):
    graph.append(list(map(int, input())))

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
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            total += 1
            house.append(bfs(i, j))

print(total)
house.sort()
for i in range(total):
    print(house[i])
