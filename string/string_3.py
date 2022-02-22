res = []

while True:
    str = []
    lower_str = []
    sorted_str = []
    n = int(input())

    if n == 0:
        break
    else:
        for i in range(n):
            str.append(input())
        lower_str = [i.lower() for i in str]
        sorted_str = sorted(lower_str)
        index = lower_str.index(sorted_str[0])
        res.append(str[index])

for i in res:
    print(i)