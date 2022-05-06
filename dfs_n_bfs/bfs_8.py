from collections import deque

M, N = map(int, input().split())
box = []

for i in range(N):
    box.append(list(map(int, input().split())))

q = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i, j])

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny]==0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

bfs()
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)

print(max(map(max, box))-1)