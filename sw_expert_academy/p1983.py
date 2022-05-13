N, target = map(int, input().split())

scores = []
for i in range(N):
    m, f, a = map(int, input().split())
    score = m * 0.35 + f * 0.45 + a * 0.2
    scores.append([i+1, score])
rank = sorted(scores, key=lambda x : -x[1])

sec = N // 10
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for j in range(N):
    rank[j].append(grade[j//sec])

for k in range(N):
    if rank[k][0] == target:
        print(rank[k][2])