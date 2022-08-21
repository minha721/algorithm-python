T = int(input())

for tc in range(T):
    N = int(input())
    s = ''
    for _ in range(N):
        c, cnt = map(str, input().split())
        s += c * int(cnt)

    print("#{}".format(tc + 1))
    for i in range(0, len(s), 10):
        print(s[i:i+10])