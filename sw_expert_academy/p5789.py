N, Q = map(int, input().split())
box = [0] * N

for i in range(Q):
    L, R = map(int, input().split())
    for j in range(L-1, R):
        box[j] = i + 1

for i in box:
    print(i, end=' ')