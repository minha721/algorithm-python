n = int(input())

score = []
for i in range(n):
    score.append(int(input()))

if n == 1:
    print(score[0])
else:
    dp = [0]*(n+1)
    dp[1] = score[0]
    dp[2] = score[0] + score[1]

    for i in range(3, n+1):
        dp[i] = max(score[i-1]+score[i-2]+dp[i-3], score[i-1]+dp[i-2])

    print(dp[n])