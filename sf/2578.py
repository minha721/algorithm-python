bingo = [list(map(int, input().split())) for _ in range(5)]
host = sum([list(map(int, input().split())) for _ in range(5)], [])

for idx, num in enumerate(host):
    # 사회자가 부른 번호의 x, y 좌표값 알아내서 visit 처리
    x, y = [(i, j) for i in range(5) for j in range(5) if bingo[i][j] == num].pop()
    bingo[x][y] = 0

    if idx < 11:
        continue
    else:
        cnt = 0

        # 행별로 확인하면서 5개 수 지워지면 cnt 증가
        for row in bingo:
            if row.count(0) == 5:
                cnt += 1

        # 열별로 확인하면서 5개 수 지워지면 cnt 증가
        for col in list(map(list, zip(*bingo))):
            if col.count(0) == 5:
                cnt += 1

        # 양쪽 대각선 확인
        r = 0
        l = 0
        for n in range(5):
            r += bingo[n][n]
            l += bingo[n][4 - n]

        if r == 0:
            cnt += 1
        if l == 0:
            cnt += 1

        # 다 확인하고 3개 이상되면 몇번째인지 출력
        if cnt >= 3:
            print(idx + 1)
            break
        else:
            continue