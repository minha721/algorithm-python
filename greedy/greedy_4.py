n = int(input())
arr = str(input())


def firstBlue():
    flag = 0
    cnt = 1
    for i in arr:
        if i == 'R':
            if flag == 0:
                cnt += 1
                flag = 1
        else:
            flag = 0
    return cnt


def firstRed():
    flag = 1
    cnt = 1
    for i in arr:
        if i == 'B':
            if flag == 1:
                cnt += 1
                flag = 0
        else:
            flag = 1
    return cnt


print(min(firstBlue(), firstRed()))
