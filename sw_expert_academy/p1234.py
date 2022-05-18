L, N = map(str, input().split())
number = list(N)

while True:
    i = 1
    before = number[0]
    remove = []

    while True:
        if i >= len(number):
            break
        else:
            if before == number[i]:
                remove.append(i - 1)
                remove.append(i)
                if i < len(number) - 1:
                    before = number[i + 1]
                i += 2
            else:
                before = number[i]
                i += 1
    if len(remove) == 0:
        break
    else:
        for i in range(len(remove)):
            index = remove[i] - i
            del number[index]

print(''.join(number))