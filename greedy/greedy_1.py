cnt = 0

n = int(input())

while True:
    if n == 1 or n == 3:
        print(-1)
        break

    if n % 5 == 0:
        cnt += (n//5)
        print(cnt)
        break
    else:
        n -= 2
        cnt += 1
