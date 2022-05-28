T = int(input())

for tc in range(1, T+1):
    data, cnt = input().split() # 숫자판의 정보, 교환횟수
    cnt = int(cnt)

    now = set([data])
    changed = set()

    for th in range(cnt): # change 만큼 한 자리씩 바꿔나감
        while now: # now에는 th 자리만큼 교환된 숫자가 포함되어 있음
            s = list(now.pop())
            for i in range(len(data)):
                for j in range(i+1, len(data)):
                    s[i], s[j] = s[j], s[i]
                    changed.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
            # now에서 하나씩 꺼내 한자리씩 바꾼 것을 nxt에 저장
        # th + 1 자리만큼 변경이 완료, 빈 now와 자리를 바꾼 것을 저장한 nxt를 바꿈
        now, changed = changed, now
    print('#{} {}'.format(tc, max(map(int, now))))