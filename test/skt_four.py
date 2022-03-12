from collections import deque

def distance(n, graph, i, j):
    visited = [False] * (n+1)
    visited[i] = True
    queue = deque()
    queue.append((0, i))

    def bfs():
        while queue:
            cnt, x = queue.popleft()

            for i in graph[x]:
                if not visited[i]:
                    if i == j:
                        return cnt+1
                    else:
                        visited[i] = True
                        queue.append((cnt+1, i))
        return -1

    return bfs()

def solution(n, edges):
    graph = [[] for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    answer = 0

    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    for i in range(n):
        for j in range(n):
            dist[i][j] = distance(n, graph, i, j)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] + dist[j][k] == dist[i][k]:
                    answer += 1
    
    return answer

print(solution(4, [[2,3],[0,1],[1,2]]))