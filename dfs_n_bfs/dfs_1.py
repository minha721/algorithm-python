# simple dfs

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
 
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
    [5]
]
 
# 각 노드가 방문된 정보를 표현
visited = [False]*10
 
dfs(graph, 1, visited)