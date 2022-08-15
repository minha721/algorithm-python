tw,th = map(int, input().split())
N = int(input())
w = [0, tw]
h = [0, th]

for _ in range(N):
    line, num = map(int, input().split())
    if line == 0:
        h.append(num)
    else:
        w.append(num)

w.sort()
h.sort()
res = -1

for i in range(1, len(w)):
    for j in range(1, len(h)):
        res = max(res, (w[i] - w[i-1])*(h[j] - h[j-1]))

print(res)