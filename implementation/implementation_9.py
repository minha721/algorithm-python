H, W = map(int, input().split())
world = list(map(int, input().split()))
total = 0

for i in range(1, W-1):
    # left는 시작~i-1, right는 i+1~끝 중에 가장 큰 값
    left = max(world[:i])
    right = max(world[i+1:])
    standard = min(left, right)

    if standard >= world[i]:
        total += ((standard-world[i]) * 1)

print(total)