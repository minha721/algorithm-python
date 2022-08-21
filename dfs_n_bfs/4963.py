def dfs(y, x):
    visited[y][x] = True

    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < w and 0 <= ny < h:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny, nx)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        graph = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        cnt = 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if not visited[i][j] and graph[i][j] == 1:
                    cnt += 1
                    dfs(i, j)

    print(cnt)