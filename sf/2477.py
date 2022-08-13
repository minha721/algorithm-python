K = int(input())
s = []
farm = [[] for _ in range(4)]
sWidth, sHeight, lWidth, lHeight = 0, 0, 0, 0

for _ in range(6):
    n, l = map(int, input().split())
    s.append([n, l])
    farm[n - 1].append(l)

for i in range(len(farm)):
    if len(farm[i]) == 1 and i <= 2:
        lHeight = farm[i][0]
    elif len(farm[i]) == 1 and i > 2:
        lWidth = farm[i][0]

for i in range(len(s)):
    if s[i][1] == lHeight:
        if i + 3 > 5:
            sHeight = s[i + 3 - 6][1]
        else:
            sHeight = s[i + 3][1]
    if s[i][1] == lWidth:
        if i + 3 > 5:
            sWidth = s[i + 3 - 6][1]
        else:
            sWidth = s[i + 3][1]

print(K * (lWidth * lHeight - sWidth * sHeight))