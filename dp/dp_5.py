n = int(input())

d = [0] * (n+1)

if n == 1:
    d[1] = 1
    print(d[1]%10007)
else:
    d[1] = 1
    d[2] = 3

    if n == 2:
        print(d[2]%10007)
    else:
        for i in range(3, n+1):
            d[i] = 2*d[i-2] + d[i-1]

        print(d[n]%10007)