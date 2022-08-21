def dfs(v, cnt):
    global res

    if res < cnt:
        res = cnt

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    res = 0
    visited = [False for _ in range(N + 1)]
    for i in range(N + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

    print("#{} {}".format(tc+1, res))