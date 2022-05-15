N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

res = 0

for i in range(N-M+1):
    for j in range(N-M+1):
        sum = 0
        for k in range(i, i+M):
            for l in range(j, j+M):
                sum += graph[k][l]
        res = max(res, sum)

print(res)