N = int(input())
num = list(map(int, input().split()))
line = []

for i in range(N):
    line.insert(i - num[i], i + 1)

print(*line)