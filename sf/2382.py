dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
reverse = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        for i in range(len(microbe)):
            # [0] : y, [1] : x, [2] : cnt, [3] : dir
            microbe[i][0] = microbe[i][0] + dy[microbe[i][3]]
            microbe[i][1] = microbe[i][1] + dx[microbe[i][3]]

            if microbe[i][0] == 0 or microbe[i][0] == N - 1 or microbe[i][1] == 0 or microbe[i][1] == N - 1:
                microbe[i][2] //= 2
                microbe[i][3] = reverse[microbe[i][3]]

        microbe.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        j = 1
        while j < len(microbe):
            if microbe[j - 1][0:2] == microbe[j][0:2]:
                microbe[j - 1][2] += microbe[j][2]
                microbe.pop(j)
            else:
                j += 1

    answer = 0
    for m in microbe:
        answer += m[2]

    print("#{} {}".format(tc + 1, answer))