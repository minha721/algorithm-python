# simple bfs

from collections import deque


def bfs(v):
    queue = deque([v])

    while queue:
        x = queue.popleft()
        visited[x] = True
        print(x, end=" ")

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)


# 각 노드가 연결된 정보를 표현
graph = [
    [],  # 0번 노드가 없으므로 index 0은 비워둠
    [2, 3],  # 1번 노드와 연결된 노드
    [1, 4, 5],
    [1, 6, 7],
    [2, 8],
    [2, 9],
    [3],
    [3],
    [4],
    [5],
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 10

bfs(1)
