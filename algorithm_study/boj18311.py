N, K = map(int, input().split())
course = list(map(int, input().split()))
length = sum(course) - 1

if K <= length:
    num = 1
    for i in course:
        K = K - i
        if K < 0:
            break
        else:
            num += 1
else:
    K = K - length - 1
    num = N
    for i in list(reversed(course)):
        K = K - i
        if K < 0:
            break
        else:
            num -= 1

print(num)