N = int(input())

for _ in range(N):
    a_cnt = [0]*5
    b_cnt = [0]*5
    a_card = list(map(int, input().split()))[1:]
    b_card = list(map(int, input().split()))[1:]

    for card in a_card:
        a_cnt[card] += 1
    for card in b_card:
        b_cnt[card] += 1

    for i in range(1,5):
        if a_cnt[-i] > b_cnt[-i]:
            print('A')
            break
        elif a_cnt[-i] < b_cnt[-i]:
            print('B')
            break
    else:
        print('D')