N, K = map(int, input().split())
temp = list(map(int, input().split()))

kDays = [sum(temp[:K])]

for i in range(1, N - K + 1):
    kDays.append(kDays[-1] - temp[i - 1] + temp[i + K - 1])

print(max(kDays))