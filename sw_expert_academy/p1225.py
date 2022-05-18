from collections import deque

code = deque(map(int, input().split()))

decrease = 0
while True:
    if decrease == 5:
        decrease = 1
    else:
        decrease += 1
    num = code.popleft() - decrease

    if num <= 0:
        code.append(0)
        break
    else:
        code.append(num)

for i in code:
    print(i, end=' ')
print()