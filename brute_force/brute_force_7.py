from itertools import combinations

N = int(input())
taste = []

for i in range(N):
    taste.append(list(map(int, input().split())))

items = [combinations(taste, i) for i in range(1, N+1)]

sub = []

for item in items:
    for i in item:
        stotal = 1
        btotal = 0
        for S, B in i:
            stotal *= S
            btotal += B
        sub.append(abs(stotal-btotal))

print(min(sub))