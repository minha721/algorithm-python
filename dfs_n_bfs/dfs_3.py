vertex = int(input())
edge = int(input())
connect = []
graph = [[] for _ in range(vertex + 1)]
visited = [False] * (vertex + 1)

# 입력
for i in range(edge):
    connect.append(list(map(int, input().split())))

# graph에 연결 정보 저장
for i in connect:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


dfs(1)

print(visited.count(True) - 1)
