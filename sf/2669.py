rectangle = [list(map(int, input().split())) for _ in range(4)]
graph = [[0] * 100 for _ in range(100)]

for lbx, lby, rtx, rty in rectangle:
    for i in range(lbx, rtx):
        for j in range(lby, rty):
            graph[i][j] = 1

print(sum(graph, []).count(1))