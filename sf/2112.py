def comb(depth, k, cnt):
    global answer

    if depth >= answer:
        return

    if depth == cnt:
        if check(temp):
            answer = min(answer, depth)
        return

    for i in range(k, D):
        for j in range(2):
            temp[i] = drugs[j]
            comb(depth + 1, i + 1, cnt)
            temp[i] = cells[i]


def check(cur_cells):
    for c in range(W):
        cnt = 1
        for r in range(D - 1):
            if cur_cells[r][c] == cur_cells[r + 1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True


T = int(input())
for tc in range(T):
    # 두께, 가로길이, 합격 기준
    D, W, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(D)]

    drugs = [[0] * W, [1] * W]
    temp = [c[:] for c in cells]

    if check(cells):
        answer = 0

    else:
        answer = 1e9
        for i in range(1, D + 1):
            comb(0, 0, i)

    print("#{} {}".format(tc + 1, answer))
