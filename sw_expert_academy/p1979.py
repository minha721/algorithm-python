N, K = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(str, input().split())))

# 행 문자열 만들기
row = []
for i in graph:
    row.append(''.join(i))

# 열 문자열 만들기
cGraph = list(map(list, zip(*graph)))
col = []
for i in cGraph:
    col.append(''.join(i))

cnt = 0
for i in row + col:
    t = i.split('0')
    cnt += t.count('1' * K)

print(cnt)