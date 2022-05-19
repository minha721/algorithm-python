from collections import deque

N = int(input())
cards = list(map(str, input().split()))

first = deque()
second = deque()

for i in range(N):
    if N % 2 == 0:
        if i < N//2:
            first.append(cards[i])
        else:
            second.append(cards[i])
    else:
        if i < N//2 + 1:
            first.append(cards[i])
        else:
            second.append(cards[i])

while first:
    print(first.popleft(), end=' ')
    if len(second) > 0:
        print(second.popleft(), end=' ')
print()