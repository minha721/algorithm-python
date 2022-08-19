from itertools import combinations

def getDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
res = 1e9

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

pchiken = list(combinations(chicken, M))

for c in pchiken:
    cityChicken = 0
    for x1, y1 in house:
        hmin = 1e9
        for x2, y2 in c:
            hmin = min(hmin, getDistance(x1, y1, x2, y2))
        cityChicken += hmin
    res = min(res, cityChicken)

print(res)