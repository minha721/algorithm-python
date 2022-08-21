def dfs(v, cnt):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

res = 0
visited = [False for _ in range(N + 1)]
for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i, 1)
        res += 1

print(res)