N = int(input())
res = 1

for i in range(1, N//2+1):
    sum_num = 0

    while True:
        sum_num += i
        if sum_num == N:
            res += 1
        elif sum_num > N:
            break
        else:
            i += 1

print(res)