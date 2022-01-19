from collections import deque

n = int(input())
connect = []
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

parent = [0] * (n + 1)

for i in range(n - 1):
    connect.append(list(map(int, input().split())))

for i in connect:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


def bfs(v):
    visited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                parent[i] = v
                visited[i] = True


bfs(1)

for i in range(2, len(parent)):
    print(parent[i])
