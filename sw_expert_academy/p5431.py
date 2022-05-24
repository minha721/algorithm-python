N, K = map(int, input().split())

total = set()
for i in range(N):
    total.add(i+1)

complete = set(map(int, input().split()))
incomplete = total - complete

for i in incomplete:
    print(i, end=' ')
print()