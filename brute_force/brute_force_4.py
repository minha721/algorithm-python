N = int(input())
B = []

for i in range(N):
    B.append(int(input()))

before = 1000001
cnt = 1
res_cnt = 1

for i in set(B):
    for j in B:
        if j != i:
            if before != j:
                res_cnt = max(res_cnt, cnt)
                before = j
                cnt = 1
            else:
                cnt += 1
res_cnt = max(res_cnt, cnt)

print(res_cnt)