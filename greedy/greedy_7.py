N = int(input())
time = []

for i in range(N):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda x: x[0])
time = sorted(time, key=lambda x: x[1])

end = 0
cnt = 0

for i, j in time:
    if i >= end:
        cnt += 1
        end = j

print(cnt)