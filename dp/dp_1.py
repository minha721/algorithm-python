N = int(input())

d = [5001] * (N+3)
d[3] = 1
d[5] = 1

for i in range(6, N+1) :
    d[i] = min(d[i-3]+1, d[i-5]+1)

if d[N] >= 5001:
    print(-1)
else:
    print(d[N])