T = int(input())

for test_case in range(1, T + 1):
    string = input()
    first = string[0]

    for i in range(1, 10):
        if string[i] == first:
            if string[0:i] == string[i:i + i]:
                print("#{} {}".format(test_case, i))
                break