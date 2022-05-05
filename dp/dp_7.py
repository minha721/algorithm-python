n = int(input())

amount = []
for i in range(n):
    amount.append(int(input()))

if n == 1:
    print(amount[0])
elif n == 2:
    print(amount[0] + amount[1])
else:
    d = [0] * n
    d[0] = amount[0]
    d[1] = amount[0] + amount[1]
    d[2] = max(amount[0]+amount[2], amount[1]+amount[2], amount[0]+amount[1])

    if n > 3:
        for i in range(3, n):
            d[i] = max(amount[i]+amount[i-1]+d[i-3], amount[i]+d[i-2], d[i-1])

    print(max(d))