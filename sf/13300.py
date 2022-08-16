N, K = map(int, input().split())
inp = [list(map(int, input().split())) for i in range(N)]
student = [[] for i in range(6)]
cnt = [[0, 0] for i in range(6)]
res = 0

for i in inp:
    student[i[1]-1].append(i[0])

for i in range(len(student)):
    for j in student[i]:
        if j == 1:
            cnt[i][1] += 1
        else:
            cnt[i][0] += 1

for i in sum(cnt, []):
    if i % K == 0:
        res += (i // K)
    else:
        res += (i // K + 1)

print(res)