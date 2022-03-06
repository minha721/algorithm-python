from collections import deque

n = int(input())
one, two = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
visited[one] = True
queue = deque()
queue.append((0, one))

def bfs():
    while queue:
        cnt, x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                if i == two:
                    return cnt+1
                else:
                    visited[i] = True
                    queue.append((cnt+1, i))
    return -1

print(bfs())