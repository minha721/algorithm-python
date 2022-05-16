N = 100
graph = []
sums = []

# 입력과 동시에 각 행의 합 구하기
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    sums.append(sum(row))

# 각 열의 합 구하기
for j in range(N):
    scol = 0
    for k in range(N):
        scol += graph[k][j]
    sums.append(scol)

# 오른대각선 합 구하기
r, c = 0, 0
rline = 0
while True:
    if r>=N or c>=N:
        sums.append(rline)
        break
    rline += graph[r][c]
    r += 1
    c += 1

# 왼대각선 합 구하기
r, c = 99, 99
lline = 0
while True:
    if r<0 or c<0:
        sums.append(lline)
        break
    lline += graph[r][c]
    r -= 1
    c -= 1

print(max(sums))