T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    for i in range(1, N+1):
        cnt = str(i).count("3") + str(i).count("6") + str(i).count("9")
        if cnt == 0:
            print(i, end=' ')
        else:
            print("-"*cnt, end=' ')

    print()