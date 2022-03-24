from itertools import permutations

items = [str(i) for i in range(1, 10)]
num = list(permutations(items, 3))

T = int(input())

for i in range(T):
    n, s, b = map(int, input().split())
    n = list(str(n))
    cntDel = 0
    for j in range(len(num)):
        strike = 0
        ball = 0
        j -= cntDel
        for k in range(3):
            if num[j][k]==n[k]:
                strike += 1
            elif n[k] in num[j]:
                ball += 1
        if (strike!=s) or (ball!=b):
            num.remove(num[j])
            cntDel += 1

print(len(num))