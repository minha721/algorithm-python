w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dw = [i for i in range(w)]
for i in range(w, 0, -1):
    dw.append(i)

dh = [i for i in range(h)]
for i in range(h, 0, -1):
    dh.append(i)

resP = dw[(p + t) % (2 * w)]
resQ = dh[(q + t) % (2 * h)]

print(resP, resQ)