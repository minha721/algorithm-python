N = int(input())
power = []
for i in range(N-1):
    power.append(list(map(int, input().split())))
K = int(input())

if N == 1:
    print(0)
elif N == 2:
    print(power[0][0])
else:
    d = [0]* N
    d[1] = power[0][0]

    for i in range(2, N):
        d[i] = min(d[i-1]+power[i-1][0], d[i-2]+power[i-2][1])

    res = d[-1]

    for i in range(3, N):
        d_copy = d[:]
        # i번째에서 K를 썼을 때
        d_copy[i] = min(d_copy[i], d_copy[i-3] + K)
        for j in range(i+1, N):
            d_copy[j] = min(d_copy[j-1]+power[j-1][0], d_copy[j-2]+power[j-2][1])
        res = min(res, d_copy[-1])

    print(res)