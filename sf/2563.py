N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * 100 for _ in range(100)]

for bx, by in paper:
    for i in range(bx, bx+10):
        for j in range(by, by+10):
            graph[i][j] = 1

print(sum(graph, []).count(1))