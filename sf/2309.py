from itertools import combinations

height = [int(input()) for _ in range(9)]
comb = list(combinations(height, 7))

for i in comb:
    if sum(i) == 100:
        res = sorted(list(i))
        for j in res:
            print(j)
        break