n = int(input())

T = []
P = []
dp = [0] * (n + 1)

for i in range(n):
    inpt, inpp = map(int, input().split())
    T.append(inpt)
    P.append(inpp)

for i in range(n - 1, -1, -1):
    if T[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])

print(dp[0])