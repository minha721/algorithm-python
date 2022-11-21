T = int(input())

for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    yx = (dy + dx) // 2
    answer = 2 * yx + abs(dx - yx) + abs(dy - yx)
    print("#{} {}".format(tc + 1, answer))