T = int(input())

for i in range(T):
    N = int(input())
    score = []
    for i in range(N):
        score.append(list(map(int, input().split())))

    score = sorted(score, key=lambda x:x[0])

    cnt = 0
    cur = N + 1
    for i, j in score:
        if j < cur:
            cnt += 1
            cur = j
    
    print(cnt)