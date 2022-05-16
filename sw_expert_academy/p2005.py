N = int(input())

graph = []
for i in range(N):
    graph.append([0]*(i+1))

for j in range(N):
    for k in range(j+1):
        if k==0 or k==j:
            graph[j][k] = 1
        else:
            graph[j][k] = graph[j-1][k-1] + graph[j-1][k]

for u in graph:
    for v in u:
        print(v, end=' ')
    print()