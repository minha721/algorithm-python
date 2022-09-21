from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.pop()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
                if cheese[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                elif cheese[ny][nx] == 1:
                    visited[ny][nx] = True
                    target.append((ny, nx))

H, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(H)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0
cnt = []

while True:
    target = []
    visited = [[False] * W for _ in range(H)]
    cnt.append(sum(cheese, []).count(1))

    visited[0][0] = True
    bfs(0, 0)

    if len(target) == 0:
        break

    for ty, tx in target:
        cheese[ty][tx] = 0

    answer += 1

print(answer)
print(cnt[-2])