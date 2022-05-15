N = int(input())
graph = []
for row in range(N):
    r = input()
    graph.append(list(r))

sum = 0
for i in range(N):
    if i <= N // 2:
        dis = i
    else:
        dis = N - i - 1
    for j in range(N//2-dis, N//2+dis+1):
        sum += int(graph[i][j])

print(sum)