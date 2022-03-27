N = input()
cnt = [0] * 10

for i in N:
    cnt[int(i)] += 1

cnt[6] = int((cnt[9] + cnt[6]) / 2 + 0.5)
cnt[9] = 0

print(max(cnt))