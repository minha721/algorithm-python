N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

sum = 0
for i in coin:
    if K >= i:
        sum += (K//i)
        K %= i
    if K == 0:
        print(sum)
        break