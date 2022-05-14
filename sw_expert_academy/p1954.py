from collections import deque

N = int(input())
graph = [[0]*N for i in range(N)]
visited = [[False]*N for i in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    mTarget = 0
    num = 1
    graph[x][y] = num

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        nx = x + dx[mTarget]
        ny = y + dy[mTarget]

        visitedOne = sum(visited, [])
        if visitedOne.count(True) == N*N:
            break
        else:
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == True:
                if mTarget < 3:
                    mTarget += 1
                else:
                    mTarget = 0
                num += 1
                graph[x + dx[mTarget]][y + dy[mTarget]] = num
                queue.append([x + dx[mTarget], y + dy[mTarget]])
            else:
                num += 1
                graph[nx][ny] = num
                queue.append([nx, ny])

bfs(0, 0)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()