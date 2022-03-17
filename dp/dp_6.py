N = int(input())
map = [list(map(int, input().split())) for i in range(N)]

dp = [[0] * N for i in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            break

        right = j + map[i][j]
        bottom = i + map[i][j]

        if right < N:
            dp[i][right] += dp[i][j]
        if bottom < N:
            dp[bottom][j] += dp[i][j]

print(dp[N-1][N-1])