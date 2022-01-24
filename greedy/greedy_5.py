a, b = map(int, input().split())
cnt = 1


def check_a(a, b):
    if b == a:
        return True
    return False


while(True):
    if b % 10 == 1:
        b = b//10
        cnt += 1
        if check_a(a, b):
            break
    elif b % 2 == 0:
        b = b//2
        cnt += 1
        if check_a(a, b):
            break
    else:
        cnt = -1
        break

    if b < a:
        cnt = -1
        break

print(cnt)
