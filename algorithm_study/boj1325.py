from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def counting(num):
    visited = [False] * (N+1)
    queue = deque()
    visited[num] = True
    queue.append(num)
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
            
    return cnt
    
hack = []
for i in range(1, N+1):
    count = counting(i)
    hack.append(count)

max_count = max(hack)
max_list = [i for i, value in enumerate(hack) if value == max_count]
max_list.sort()

for i in max_list:
    print(i+1, end=' ')