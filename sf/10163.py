N = int(input())
inp = [list(map(int, input().split())) for _ in range(N)]

paper = []
for i in inp:
    paper.append([i[0], i[1], i[0] + i[2], i[1] + i[3]])

maxNum = max(sum(paper, []))
graph = [[0] * maxNum for _ in range(maxNum)]

num = 1
for lbx, lby, rtx, rty in paper:
    for i in range(lbx, rtx):
        for j in range(lby, rty):
            graph[i][j] = num
    num += 1

for i in range(N):
    print(sum(graph, []).count(i + 1))