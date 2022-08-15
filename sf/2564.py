def get_distance(x, y): # 북쪽에서 상점까지의 거리
    if x == 1:
        return y
    if x == 2:
        return w + h + w - y
    if x == 3:
        return w + h + w + h - y
    if x == 4:
        return w + y

w, h = map(int, input().split())
n = int(input())

d = []
for _ in range(n + 1):
    x, y = map(int, input().split())
    d.append(get_distance(x, y))

answer = 0

for i in range(n):
    ic = abs(d[-1] - d[i]) # 정방향 거리
    oc = 2 * (w + h) - ic # 반대 거리
    answer += min(ic, oc)

print(answer)